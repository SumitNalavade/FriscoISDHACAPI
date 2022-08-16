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
	type response struct {
		UnweightedGPA string `json:"unweightedGPA"`
		WeightedGPA   string `json:"weightedGPA"`
	}

	queryParams := r.URL.Query()

	username := queryParams.Get("username")
	password := queryParams.Get("password")

	pageContent := utils.GetPageContent(username, password, utils.TRANSCRIPTURL)
	doc, _ := goquery.NewDocumentFromReader(strings.NewReader(pageContent))

	foundContent := utils.FindContentFromDoc(doc, "#plnMain_rpTranscriptGroup_lblGPACum1", "#plnMain_rpTranscriptGroup_lblGPACum2")

	weightedGPA := foundContent[0].Value
	unweightedGPA := foundContent[1].Value

	responseObj := response{
		WeightedGPA:   weightedGPA,
		UnweightedGPA: unweightedGPA,
	}

	jsonResponse, _ := json.Marshal(responseObj)

	w.Header().Add("Content-Type", "application/json")
	fmt.Fprintf(w, string(jsonResponse))
}
