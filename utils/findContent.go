package utils

import (
	"github.com/PuerkitoBio/goquery"
)

type FoundContent struct {
	Name string
	Value string
}

func FindContentFromDoc(doc *goquery.Document, elements...string) []FoundContent {
	var response []FoundContent
	
	for _, elm := range elements {
		content := doc.Find(elm).Text()
		response = append(response, FoundContent{ Name: elm, Value: content })
	}

	return response
}