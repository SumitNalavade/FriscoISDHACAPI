package handler

import (
	"fmt"
	"net/http"
)

func HomeHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprint(w, `
		<h1>Frisco ISD HAC API</h1>
		<p>Documentation:</p>
		<a href="https://friscoisdhacapidocs.vercel.app/" target="_blank">friscoisdhacapidocs.vercel.app</a>
	`)
}
