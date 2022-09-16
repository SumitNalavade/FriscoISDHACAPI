import React, { useState } from "react";

import { CopyBlock, solarizedLight } from "react-code-blocks";

import Drawer from "../components/drawer";
import Layout from "../components/layout";

import apiRoutes from "../utils/apiRoutes";
import IAPIRoute from "../utils/apiRouteInterface";

interface Props {
  route: IAPIRoute;
}

const Route: React.FC<Props> = ({ route }) => {
  const [testQueryParameters, setTestQueryParameters] = useState({})

  const handleTestQueryParameterChange = (parameterName: string, value: string) => {
    const testQueryParmeters = { ...testQueryParameters }
    //@ts-ignore
    testQueryParameters[parameterName] = value
    
    setTestQueryParameters(testQueryParameters)
  }

  const url = route.queryParameters.reduce((previousValue, currentValue) => previousValue + `${currentValue.title}={${currentValue.title}}&`, `${route.type} /api/${route.id}?`).slice(0, -1)

  return (
    <Layout>
      <div className="lg:grid lg:grid-cols-5 h-full">
        <Drawer />
        <div className="lg:col-span-4 p-8">
          <h2 className="text-4xl text-headline font-bold"><span className={`${ route.type === "GET" ? "text-highlight" : "text-tertiary" }`}>[{route.type}]</span> {route.title}</h2>
          <p className="text-lg py-4" >{route.description}</p>

          <CopyBlock
            language="javascript"
            text={url}
            showLineNumbers={false}
            theme={solarizedLight}
            wrapLines={true}
            codeBlock
          />

        <h3 className="text-2xl font-bold mt-10 text-headline">Query Parameters</h3>
        <table className="table-fixed my-4 text-center">
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
                  <input type="text" className="text-center border rounded-md p-2" placeholder={queryParameter.title} onChange={(e) => handleTestQueryParameterChange(queryParameter.title, e.target.value)}  />
                </td>
                <td className="p-4 border">{queryParameter.type}</td>
                <td className="p-4 border">{queryParameter.description}</td>
                <td className="p-4 border">{String(queryParameter.required).toUpperCase()}</td>
              </tr>
            ))}
          </tbody>
        </table>
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
