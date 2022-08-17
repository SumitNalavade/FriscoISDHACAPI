package handler

import (
	"net/http"
	"fmt"
)

func HomeHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, `
		<h1>Frisco ISD HAC API</h1>
		<p>Documentation:</p>
		<a>https://fisdhacapi.netlify.app/</a>
	`)
}