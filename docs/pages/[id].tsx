import React from "react";

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
        <div className="col-span-4">{route.title}</div>
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
