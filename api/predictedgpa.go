package handler

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"
)

type predictionRequestCourse struct {
	Name    string  `json:"name"`
	Grade   float32 `json:"grade"`
	Weight  float32 `json:"weight"`
	Credits float32 `json:credits`
}

type predictionRequestBody struct {
	WeightedGPA    float32                   `json:"weightedGPA"`
	UnweightedGPA  float32                   `json:"unweightedGPA"`
	StudentGrade   int8                      `json:"studentGrade"`
	CurrentClasses []predictionRequestCourse `json:"currentClasses"`
}

type predictionResponse struct {
	UnweightedGPA float32 `json:"finalUnweightedGPA"`
	WeightedGPA   float32 `json:"finalWeightedGPA"`
}

func predictGPA(currentWeightedGPA, currentUnweightedGPA float32, studentGrade int8, currentClasses []predictionRequestCourse) (float32, float32) {
	var finalWeightedGPA float32
	var finalUnweightedGPA float32

	var weightedGPAList []float32
	var unweightedGPAList []float32

	var totalCredits float32

	var pastSemesters float32 = float32((studentGrade-8)*2) - 1

	for _, course := range currentClasses {
		totalCredits += course.Credits

		var weightedGPA float32 = 0
		var unweightedGPA float32 = 0

		if course.Grade < 70 {
			weightedGPA = 0
			unweightedGPA = 0
		} else if course.Grade == 70 {
			weightedGPA = 3
			unweightedGPA = 2
		} else {
			weightedGPA = ((course.Weight - ((100 - course.Grade) / 10)) * course.Credits)
			unweightedGPA = ((4.0 - ((90 - course.Grade) / 10)) * course.Credits)

			if course.Credits == 2 && unweightedGPA > 8 {
				unweightedGPA = 8.0
			} else if unweightedGPA > 4 {
				unweightedGPA = 4
			}
		}

		weightedGPAList = append(weightedGPAList, weightedGPA)
		unweightedGPAList = append(unweightedGPAList, unweightedGPA)
	}

	for i := 0; i < len(weightedGPAList); i++ {
		finalWeightedGPA += weightedGPAList[i]
		finalUnweightedGPA += unweightedGPAList[i]
	}
	finalWeightedGPA /= totalCredits
	finalUnweightedGPA /= totalCredits

	finalWeightedGPA = (((currentWeightedGPA) * pastSemesters) + finalWeightedGPA) / (pastSemesters + 1)
	finalUnweightedGPA = (((currentUnweightedGPA) * pastSemesters) + finalUnweightedGPA) / (pastSemesters + 1)

	return finalWeightedGPA, finalUnweightedGPA
}

func PredictionHandler(w http.ResponseWriter, r *http.Request) {
	requestBodyString, _ := io.ReadAll(r.Body)

	requestData := predictionRequestBody{}
	json.Unmarshal([]byte(string(requestBodyString)), &requestData)

	weightedGPA, unweightedGPA := predictGPA(requestData.WeightedGPA, requestData.UnweightedGPA, requestData.StudentGrade, requestData.CurrentClasses)

	responseObj := predictionResponse{
		UnweightedGPA: unweightedGPA,
		WeightedGPA:   weightedGPA,
	}

	response, _ := json.Marshal(responseObj)

	w.Header().Add("Content-Type", "application/json")
	fmt.Fprint(w, string(response))
}
