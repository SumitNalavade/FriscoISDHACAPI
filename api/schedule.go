package handler

import (
	"encoding/json"
	"fmt"
	"net/http"
	"strings"

	"github.com/PuerkitoBio/goquery"
	"github.com/SumitNalavade/FRISCOISDHACAPIV2/utils"
)

func ScheduleHandler(w http.ResponseWriter, r *http.Request) {
	var courses []utils.StudentScheduleType

	queryParams := r.URL.Query()

	username := queryParams.Get("username")
	password := queryParams.Get("password")

	if username == "john" && password == "doe" {
		response, _ := json.Marshal(utils.FakeStudentSchedule)
		w.Header().Add("Content-Type", "application/json")
		fmt.Fprint(w, string(response))
		return
	}

	pageContent := utils.GetPageContent(username, password, utils.SCHEDULEURL)
	doc, _ := goquery.NewDocumentFromReader(strings.NewReader(pageContent))

	doc.Find("tr.sg-asp-table-data-row").Each(func(i int, s *goquery.Selection) {
		var newCourse utils.StudentScheduleType

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

	response, _ := json.Marshal(courses)
	
	if(string(response) == "null") {
		w.WriteHeader(http.StatusUnauthorized)
		fmt.Fprint(w, "Something went wrong!")
		return
	}

	w.Header().Add("Content-Type", "application/json")
	fmt.Fprint(w, string(response))
}
