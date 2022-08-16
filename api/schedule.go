package handler

import (
	"encoding/json"
	"fmt"
	"net/http"
	"strings"

	"github.com/PuerkitoBio/goquery"
	"github.com/SumitNalavade/FRISCOISDHACAPIV2/utils"
)

const scheduleURL string = "https://hac.friscoisd.org/HomeAccess/Content/Student/Classes.aspx"

type scheduleResponse struct {
	Schedule []course `json:"schedule"`
}

type course struct {
	Building string `json:"building"`
	Code string `json:"courseCode"`
	Name string `json:"courseName"`
	Days string `json:"days"`
	MarkingPeriods string `json:"markingPeriods"`
	Periods string `json:"periods"`
	Room string `json:"room"`
	Status string `json:"status"`
	Teacher string `json:"teacher"`
}

func ScheduleHandler(w http.ResponseWriter, r *http.Request) {
	var courses []course

	queryParams := r.URL.Query()

	username := queryParams.Get("username")
	password := queryParams.Get("password")
	
	pageContent := utils.GetPageContent(username, password, scheduleURL)

	doc, _ := goquery.NewDocumentFromReader(strings.NewReader(pageContent))

	doc.Find("tr.sg-asp-table-data-row").Each(func(i int, s *goquery.Selection) {
		var newCourse course

		s.Find("td").Each(func(i int, s *goquery.Selection) {
			text := strings.TrimSpace(s.Text())

			switch i {
			case 0:
				newCourse.Code = text
			case 1:
				newCourse.Name = text
			case 2:
				newCourse.Periods = text
			case 3:
				newCourse.Teacher = text
			case 4:
				newCourse.Room = text
			case 5:
				newCourse.Days = text
			case 6:
				newCourse.MarkingPeriods = text
			case 7:
				newCourse.Building = text
			case 8:
				newCourse.Status = text
			}
		})

		courses = append(courses, newCourse)
 	})

	responseObj := scheduleResponse{
		Schedule: courses,
	}

	response, _ := json.Marshal( responseObj )

	w.Header().Add("Content-Type", "application/json") 
	fmt.Fprintf(w, string(response))
}