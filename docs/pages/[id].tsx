import React from "react";

import { CopyBlock, solarizedLight } from "react-code-blocks";

import Drawer from "../components/drawer";
import Layout from "../components/layout";

import apiRoutes from "../utils/apiRoutes";
import IAPIRoute from "../utils/apiRouteInterface";

interface Props {
  route: IAPIRoute;
}

const Route: React.FC<Props> = ({ route }) => {
  return (
    <Layout>
      <div className="grid grid-cols-5 h-full">
        <Drawer />
        <div className="col-span-4 p-8">
          <h2 className="text-4xl text-headline font-bold"><span className={`${ route.type === "GET" ? "text-highlight" : "text-tertiary" }`}>[{route.type}]</span> {route.title}</h2>
          <p className="text-lg py-4" >{route.description}</p>

          <CopyBlock
            language="javascript"
            text="GET /students/pastassignments?username={username}&password={password}&quarter={quarter}"
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
