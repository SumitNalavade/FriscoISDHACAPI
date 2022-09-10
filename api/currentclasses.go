package handler

import (
	"encoding/json"
	"fmt"
	"net/http"
	"strings"

	"github.com/PuerkitoBio/goquery"

	"github.com/SumitNalavade/FRISCOISDHACAPIV2/utils"
)

func CurrentClassesHandler(w http.ResponseWriter, r *http.Request) {
	var courses []utils.StudentCourseType

	queryParams := r.URL.Query()

	username := queryParams.Get("username")
	password := queryParams.Get("password")

	if username == "john" && password == "doe" {
		response, _ := json.Marshal(utils.FakeStudentCurrentClasses)
		w.Header().Add("Content-Type", "application/json")
		fmt.Fprintf(w, string(response))
		return
	}
	
	pageContent := utils.GetPageContent(username, password, utils.CLASSESURL)
	doc, _ := goquery.NewDocumentFromReader(strings.NewReader(pageContent))

	doc.Find(".AssignmentClass").Each(func(i int, s *goquery.Selection) {
		var newCourse utils.StudentCourseType

		newCourse.Name = strings.TrimSpace(s.Find("a.sg-header-heading").Text())
		newCourse.Grade = strings.TrimSpace(s.Find("span.sg-header-heading").Text())
		newCourse.LastUpdated = strings.Replace(strings.Replace(strings.TrimSpace(s.Find(".sg-header-sub-heading").Text()), "(Last Updated: ", "", 1), ")", "", 1)

		s.Find(".sg-asp-table-data-row").Each(func(i int, s *goquery.Selection) {
			var newAssignment utils.StudentAssignmentType

			s.Find("td").Each(func(i int, s *goquery.Selection) {
				text := strings.TrimSpace(s.Text())
				switch i {
				case 0:
					newAssignment.DateDue = text
				case 1:
					newAssignment.DateAssigned = text
				case 2:
					newAssignment.Name = strings.TrimSpace(strings.Replace(text, "*", "", 1))
				case 3:
					newAssignment.Category = text
				case 4:
					newAssignment.Score = text
				case 5:
					newAssignment.TotalPoints = text
				}
			})
			newCourse.Assignments = append(newCourse.Assignments, newAssignment)
		})

		courses = append(courses, newCourse)
	})

	fmt.Fprintf(w, "success")
}