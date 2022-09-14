import IAPIRoute from "./apiRouteInterface";

const APIRoutes: IAPIRoute[] = [
    {
        type: "GET",
        id: "info",
        title: "Student Info",
        description: "Get a student's registration information from HAC (Name, Grade, Counselors etc...)",
        queryParameters: [
            {
                title: "Username",
                type: "string",
                description: "HAC Username",
                required: true
            }
        ],
        exampleRequest: `axios.get("https://gradual-deploy.vercel.app/students/info?username=john&password=doe").then((res) => {
            console.log(res.data);
        }).catch((error) => {
            console.log(error);
        })`,
        exampleResponse: `
        {
            "studentBirthDate": "12/24/2003",
            "studentBuilding": "Heritage High School",
            "studentGrade": "12",
            "studentID": "123456",
            "studentName": "Jonh Doe"
        }`
    },
    {
        type: "GET",
        id: "gpa",
        title: "Student GPAs",
        description: "Get a student's most recently published weighted and unweighted GPA from HAC",
        queryParameters: [
            {
                title: "Username",
                type: "string",
                description: "HAC Username",
                required: true
            }
        ],
        exampleRequest: `https://gradual-deploy.vercel.app/students/gpa?username=john&password=doe").then((res) => {
            console.log(res.data);
        }).catch((error) => {
            console.log(error);
        })`,
        exampleResponse: `
        {
            "unweightedGPA" : "3.8800",
            "weightedGPA" : "5.0500"
        }`
    }
]

export default APIRoutes;