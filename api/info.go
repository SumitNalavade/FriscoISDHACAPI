package handler

import (
	"encoding/json"
	"fmt"
	"net/http"
	"strings"

	"github.com/PuerkitoBio/goquery"

	"github.com/SumitNalavade/FRISCOISDHACAPIV2/utils"
)

const registrationPageURL string = "https://hac.friscoisd.org/HomeAccess/Content/Student/Registration.aspx"

type infoResponse struct {
    Birthdate string `json:"birthdate"`
    Campus string `json:"campus"`
	Counselor string `json:"counselor"`
	Grade string `json:"grade"`
	ID string `json:"id"`
	Name string `json:"name"`
}

func InfoHandler(w http.ResponseWriter, r *http.Request) {
	queryParams := r.URL.Query()

	username := queryParams.Get("username")
	password := queryParams.Get("password")

	pageContent := utils.GetPageContent(username, password, registrationPageURL)

	doc, _ := goquery.NewDocumentFromReader(strings.NewReader(pageContent))

	studentBirthDate := utils.FindFromDoc(doc, "#plnMain_lblBirthDate").Text()
	studentCampus := utils.FindFromDoc(doc, "#plnMain_lblBuildingName").Text()
	studentCounselor := utils.FindFromDoc(doc, "#plnMain_lblCounselor").Text()
	studentGrade := utils.FindFromDoc(doc, "#plnMain_lblGrade").Text()
	studentID := utils.FindFromDoc(doc, "#plnMain_lblRegStudentID").Text()
	studentName := utils.FindFromDoc(doc, "#plnMain_lblRegStudentName").Text()

	responseObj := infoResponse{
		Birthdate: studentBirthDate,	
		Campus : studentCampus,
		Counselor: studentCounselor,
		Grade: studentGrade,
		ID: studentID,
		Name: studentName,
	}

	response, _ := json.Marshal( responseObj )

	w.Header().Add("Content-Type", "application/json")
	fmt.Fprintf(w, string(response))
}