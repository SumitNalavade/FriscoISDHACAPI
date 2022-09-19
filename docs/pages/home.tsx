import React from "react";

import Layout from "../components/layout";
import Drawer from "../components/drawer";

import { CopyBlock, solarizedLight } from "react-code-blocks";
     
const Home: React.FC = () => {
    return (
        <Layout>
            <div className="lg:grid lg:grid-cols-5 h-full">
                <Drawer />
                <div className="lg:col-span-4 p-8">
                    <h3 className="text-4xl text-headline font-bold">Get Started</h3>

                    <h3 className="text-2xl font-bold mt-10 mb-2 text-headline">Base API URL</h3>
                    <CopyBlock
                        language="javascript"
                        text="https://friscoisdhacapi.vercel.app"
                        showLineNumbers={false}
                        theme={solarizedLight}
                        wrapLines={true}
                        codeBlock
                    />
                </div>
            </div>
        </Layout>
    )
}

export default Home;