interface IQueryParameter {
    title: string
    type: "string" | "number" | "boolean"
    description: string
    required?: boolean
}

export default interface IAPIRoute {
    type: "GET" | "POST"
    id: string
    title: string
    description: string
    queryParameters: IQueryParameter[]
    exampleRequest: string
    exampleResponse: string
}