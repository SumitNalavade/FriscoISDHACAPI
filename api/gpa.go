package handler

import (
	"encoding/json"
	"fmt"
	"net/http"
	"strings"

	"github.com/PuerkitoBio/goquery"

	"github.com/SumitNalavade/FRISCOISDHACAPIV2/utils"
)

const transcriptPageURL string = "https://hac.friscoisd.org/HomeAccess/Content/Student/Transcript.aspx"

type gpaResponse struct {
    UnweightedGPA string `json:"unweightedGPA"`
	WeightedGPA string `json:"weightedGPA"`
}

func GPAHandler(w http.ResponseWriter, r *http.Request) {
	queryParams := r.URL.Query()

	username := queryParams.Get("username")
	password := queryParams.Get("password")

	pageContent := utils.GetPageContent(username, password, transcriptPageURL)

	doc, _ := goquery.NewDocumentFromReader(strings.NewReader(pageContent))

	weightedGPA := utils.FindFromDoc(doc, "#plnMain_rpTranscriptGroup_lblGPACum1").Text()
	unweightedGPA := utils.FindFromDoc(doc, "#plnMain_rpTranscriptGroup_lblGPACum2").Text()

	responseObj := gpaResponse{
		WeightedGPA: weightedGPA,
		UnweightedGPA: unweightedGPA,
	}

	response, _ := json.Marshal( responseObj )

	w.Header().Add("Content-Type", "application/json")
	fmt.Fprintf(w, string(response))
}