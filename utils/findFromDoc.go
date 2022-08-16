package utils

import "github.com/PuerkitoBio/goquery"

func FindFromDoc(doc *goquery.Document, identifier string) *goquery.Selection {
	return doc.Find(identifier)
}