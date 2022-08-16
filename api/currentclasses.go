package handler

import (
	"fmt"
	"net/http"

	"github.com/go-resty/resty/v2"
)


func CurrentClassesHandler(w http.ResponseWriter, r *http.Request) {
	var restyClient = resty.New()

	queryParams := r.URL.Query()

	username := queryParams.Get("username")
	password := queryParams.Get("password")

	apiURL := fmt.Sprintf("https://gradualgrades.herokuapp.com/students/currentclasses?username=%v&password=%v", username, password)

	apiResponse, _ := restyClient.R().
			EnableTrace().
			Get(apiURL)

	w.Header().Add("Content-Type", "application/json") 
	fmt.Fprintf(w, apiResponse.String())
}