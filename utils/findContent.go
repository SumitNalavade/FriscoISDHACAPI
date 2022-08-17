package utils

import (
	"sync"

	"github.com/PuerkitoBio/goquery"
)

type FoundContent struct {
	Name string
	Value string
}

func FindContentFromDoc(doc *goquery.Document, elements...string) []FoundContent {
	wg := new(sync.WaitGroup)
	wg.Add(len(elements))

	var response []FoundContent
	
	for _, elm := range elements {
		go func(elm string) {
			defer wg.Done()

			content := doc.Find(elm).Text()
			response = append(response, FoundContent{ Name: elm, Value: content })
		}(elm)

		content := doc.Find(elm).Text()
		response = append(response, FoundContent{ Name: elm, Value: content })
	}

	wg.Wait()

	return response
}