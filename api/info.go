package handler

import (
	"encoding/json"
	"fmt"
	"net/http"
	"strings"

	"github.com/PuerkitoBio/goquery"

	"github.com/SumitNalavade/FRISCOISDHACAPIV2/utils"
)

func InfoHandler(w http.ResponseWriter, r *http.Request) {
	queryParams := r.URL.Query()

	username := queryParams.Get("username")
	password := queryParams.Get("password")

	if username == "john" && password == "doe" {
		response, _ := json.Marshal(utils.FakeStudentInfo)
		w.Header().Add("Content-Type", "application/json")
		fmt.Fprint(w, string(response))
		return
	}

	pageContent := utils.GetPageContent(username, password, utils.REGISTRATIONURL)
	doc, _ := goquery.NewDocumentFromReader(strings.NewReader(pageContent))

	foundContent := utils.FindContentFromDoc(doc, "#plnMain_lblBirthDate", "#plnMain_lblBuildingName", "#plnMain_lblCounselor", "#plnMain_lblGrade", "#plnMain_lblRegStudentID", "#plnMain_lblRegStudentName")

	studentBirthDate := foundContent[0].Value
	studentCampus := foundContent[1].Value
	studentCounselor := foundContent[2].Value
	studentGrade := foundContent[3].Value
	studentID := foundContent[4].Value
	studentName := foundContent[5].Value

	response, _ := json.Marshal(utils.StudentInfoType{
		Birthdate: studentBirthDate,
		Campus:    studentCampus,
		Counselor: studentCounselor,
		Grade:     studentGrade,
		ID:        studentID,
		Name:      studentName,
	})

	w.Header().Add("Content-Type", "application/json")
	fmt.Fprint(w, string(response))
}
