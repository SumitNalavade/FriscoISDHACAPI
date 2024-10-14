import React, { useState, useEffect } from "react";
import { useRouter } from 'next/router'
import axios from "axios";

import { CopyBlock, solarizedLight } from "react-code-blocks";

import Drawer from "../components/drawer";
import Layout from "../components/layout";

import apiRoutes from "../utils/apiRoutes";
import IAPIRoute from "../utils/apiRouteInterface";

interface Props {
  route: IAPIRoute;
}

const Route: React.FC<Props> = ({ route }) => {
  const dynamicRoute = useRouter().asPath
  const [testQueryParameters, setTestQueryParameters] = useState<{ username: string, password: string }>({ username: "", password: "" })
  const [responseData, setResponseData] = useState(route.exampleResponse)

  const [isLoading, setIsLoading] = useState(false);
  const [isError, setIsError] = useState(false);

  useEffect(() => {
    setResponseData(route.exampleResponse)
  }, [dynamicRoute, route.exampleResponse])

  const baseUrl = route.queryParameters.reduce((previousValue, currentValue) => previousValue + `${currentValue.title}={${currentValue.title}}&`, `${route.type} /api/${route.id}?`).slice(0, -1)
  const exampleRequest = apiRoutes.filter((elm) => elm.id === route.id ? elm.exampleRequest : "")[0].exampleRequest;

  const handleTestQueryParameterChange = (parameterName: string, value: string) => {
    const testQueryParmeters = { ...testQueryParameters }

    //@ts-ignore
    testQueryParameters[parameterName] = value

    setTestQueryParameters(testQueryParameters)
  }

  const sendRequest = async () => {
    try {
      setIsLoading(true);
      setIsError(false);

      if (testQueryParameters.username === "" || testQueryParameters.password === "") return

      let url = baseUrl

      Object.keys(testQueryParameters).forEach((key) => {
        //@ts-ignore
        url = url.replace(`{${key}}`, testQueryParameters[key]).replace(`${route.type} `, "");
      })

      const response = await axios.get(url)

      if (response) {
        // @ts-ignore
        setResponseData(JSON.stringify(response.data, null, 2))
      }

      setIsLoading(false);
    } catch (error) {
      setIsError(true);
    } finally {
      setIsLoading(false);
    }
  }

  return (
    <Layout>
      <div className="lg:grid lg:grid-cols-5 h-full">
        <Drawer />
        <div className="lg:col-span-4 p-8">
          <h2 className="text-4xl text-headline font-bold"><span className="text-highlight">[{route.type}]</span> {route.title}</h2>
          <p className="text-lg py-4" >{route.description}</p>

          <CopyBlock
            language="javascript"
            text={baseUrl}
            showLineNumbers={false}
            theme={solarizedLight}
            wrapLines={true}
            codeBlock
          />

          <h3 className="text-2xl mb-4 font-bold mt-10 text-headline">Example Request</h3>
          <CopyBlock
            language="javascript"
            text={`axios.get("friscoisdhacapi.vercel.app${exampleRequest}").then((res) => {
  console.log(res.data);
}).catch((error) => {
  console.log(error);
})`}
            showLineNumbers={false}
            theme={solarizedLight}
            wrapLines={true}
            codeBlock
          />

          <div className="bg-yellow-100 border-l-4 border-yellow-500 text-yellow-700 p-4 my-4">
            <h4 className="font-bold mb-2">Warning: Use URL-safe characters in credentials</h4>
            <p className="mb-2">
              Ensure that all credentials do not contain any characters that are invalid in URLs.
              Before sending an API request from the client, you must convert invalid characters.
            </p>
            <p className="mb-2">Examples of characters to avoid and their URL-encoded equivalents:</p>
            <ul className="list-disc list-inside mb-2">
              <li># (hash) - use %23</li>
              <li>& (ampersand) - use %26</li>
              <li>+ (plus) - use %2B</li>
              <li>/ (forward slash) - use %2F</li>
              <li>@ (at symbol) - use %40</li>
            </ul>
            <p>
              Remember to URL-encode these characters before sending requests. For example,
              if a password contains &apos;#&apos;, it should be sent as &apos;%23&apos; in the API request.
            </p>

            <p>
              For example the password: &apos;Testing#123&apos; must be converted to &apos;Testing%23123&apos;
            </p>
          </div>

          <h3 className="text-2xl font-bold mt-10 text-headline">Query Parameters</h3>
          <table className="table-fixed mt-4 mb-2 text-center">
            <thead>
              <tr className="bg-slate-100">
                <th className="p-4 border">Parameter</th>
                <th className="p-4 border">Type</th>
                <th className="p-4 border">Description</th>
                <th className="p-4 border">Required</th>
              </tr>
            </thead>
            <tbody>
              {route.queryParameters.map((queryParameter, index) => (
                <tr key={index}>
                  <td className="p-4 border">
                    <input type="text" className="text-center border rounded-md p-2" placeholder={queryParameter.title} onChange={(e) => handleTestQueryParameterChange(queryParameter.title, e.target.value)} />
                  </td>
                  <td className="p-4 border">{queryParameter.type}</td>
                  <td className="p-4 border">{queryParameter.description}</td>
                  <td className="p-4 border">{String(queryParameter.required).toUpperCase()}</td>
                </tr>
              ))}
            </tbody>
          </table>
          <button onClick={sendRequest} className="bg-tertiary text-main font-bold py-2 px-6 rounded-md active:bg-rose-600">Send Request</button>

          <h3 className="text-2xl font-bold mt-10 mb-4 text-headline">Response</h3>

          <CopyBlock
            language="javascript"
            text={isLoading ? "Loading..." : isError ? "Error" : responseData}
            showLineNumbers={false}
            theme={solarizedLight}
            wrapLines={true}
            codeBlock
          />
        </div>
      </div>
    </Layout>
  );
};

export const getStaticPaths = async () => {
  const paths = apiRoutes.map((apiRoute) => ({ params: { id: apiRoute.id } }));

  return {
    paths,
    fallback: false,
  };
};

export async function getStaticProps({ params }: { params: any }) {
  const { id } = params;

  const route = apiRoutes.find((apiRoute) => apiRoute.id === id);

  return { props: { route } };
}

export default Route;
