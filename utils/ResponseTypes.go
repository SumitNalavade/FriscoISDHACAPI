package utils

type StudentInfoType struct {
	ID string `json:"id"`
	Name string `json:"name"`
	Birthdate string `json:"birthdate"`
	Campus string `json:"campus"`
	Grade string `json:"grade"`
	Counselor string `json:"counselor"`
}

type StudentGPAType struct {
	WeightedGPA string `json:"weightedGPA"`
	UnweightedGPA string `json:"unweightedGPA"`
}

type StudentScheduleType struct {
	Building string `json:"building"`
	Code string `json:"courseCode"`
	Name string `json:"courseName"`
	Days string `json:"days"`
	MarkingPeriods string `json:"markingPeriods"`
	Periods string `json:"periods"`
	Room string `json:"room"`
	Status string `json:"status"`
	Teacher string `json:"teacher"`
}

type StudentAssignmentType struct {
	Name string `json:"name"`
	Category string `json:"category"`
	DateAssigned string `json:"dateAssigned"`
	DateDue string `json:"dateDue"`
	Score string `json:"score"`
	TotalPoints string `json:"totalPoints"`
}

type StudentCourseType struct {
	LastUpdated string `json:"lastUpdated"`
	Assignments []StudentAssignmentType `json:"assignments"`
	Credits string `json:"credits"`
	Grade string `json:"grade"`
	Name string `json:"name"`
	Weight string `json:"weight"`
}