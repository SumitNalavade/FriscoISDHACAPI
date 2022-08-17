package handler

import (
	"encoding/json"
	"fmt"
	"net/http"
	"strings"

	"github.com/PuerkitoBio/goquery"

	"github.com/SumitNalavade/FRISCOISDHACAPIV2/utils"
)

func GPAHandler(w http.ResponseWriter, r *http.Request) {
	queryParams := r.URL.Query()

	username := queryParams.Get("username")
	password := queryParams.Get("password")

	if username == "john" && password == "doe" {
		response, _ := json.Marshal(utils.FakeStudentGPAs)
		w.Header().Add("Content-Type", "application/json")
		fmt.Fprintf(w, string(response))
		return
	}

	pageContent := utils.GetPageContent(username, password, utils.TRANSCRIPTURL)
	doc, _ := goquery.NewDocumentFromReader(strings.NewReader(pageContent))

	foundContent := utils.FindContentFromDoc(doc, "#plnMain_rpTranscriptGroup_lblGPACum1", "#plnMain_rpTranscriptGroup_lblGPACum2")

	weightedGPA := foundContent[0].Value
	unweightedGPA := foundContent[1].Value

	response, _ := json.Marshal(utils.StudentGPAType{
		WeightedGPA:   weightedGPA,
		UnweightedGPA: unweightedGPA,
	})

	w.Header().Add("Content-Type", "application/json")
	fmt.Fprintf(w, string(response))
}
