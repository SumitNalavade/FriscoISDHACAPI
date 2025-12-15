import React from "react";
import apiRoutes from "../utils/apiRoutes";

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

                    <h3 className="text-2xl font-bold mt-10 my-2 text-headline">Base API URL</h3>
                    <CopyBlock
                        language="javascript"
                        text="https://friscoisdhacapi.vercel.app"
                        showLineNumbers={false}
                        theme={solarizedLight}
                        wrapLines={true}
                        codeBlock
                    />

                    <h3 className="text-2xl font-bold mt-10 my-2 text-headline">Example API Request</h3>
                    <CopyBlock
                        language="javascript"
                        text={`axios.get("friscoisdhacapi.vercel.app${apiRoutes[0].exampleRequest}").then((res) => {
    console.log(res.data);
}).catch((error) => {
    console.log(error);
})`}
                        showLineNumbers={false}
                        theme={solarizedLight}
                        wrapLines={true}
                        codeBlock
                    />

                    <h3 className="text-2xl font-bold mt-10 my-2 text-headline">Example API Response</h3>
                    <CopyBlock
                        language="javascript"
                        text={apiRoutes[0].exampleResponse}
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

                    <h3 className="text-2xl font-bold mt-10 my-2 text-headline">Production Usage (Self-Host Guide)</h3>
                    <p>Because the public deployment enforces shared rate limits, you should deploy your own copy of this API for production or high-volume use.</p>
                    <p>This project is implemented using Next.js serverless API routes and Edge middleware, and works best on platforms that natively support this architecture such as Vercel.</p>
                    <p>See the <a className="underline text-blue-500" target="__blank" href="https://github.com/SumitNalavade/FriscoISDHACAPI">self-host guide on Github</a>.</p>


                    <h3 className="text-2xl font-bold mt-10 my-2 text-headline">Fair Usage Guidelines</h3>
                    <p>This API is intended to support student learning, projects, and experimentation in a fair and responsible way.</p>
                    <p>Please use the API thoughtfully by avoiding rapid or repeated requests in tight loops, and batching requests when possible.</p>
                    <p>When building applications, add short delays between requests, cache results, and use retries with exponential backoff instead of constant polling.</p>
                    <p>These limits help keep the service available for everyone. Requests that exceed fair usage thresholds may be temporarily limited.</p>


                    <h3 className="text-2xl font-bold mt-10 my-2 text-headline">Behind The Scenes</h3>
                    <p>The API uses sends HTTP POST requests to Frisco ISD HAC servers with a username and password.</p>
                    <p>If the login is authenticated, HAC responds with an HTML page with student information.</p>
                    <p>The resulting HTML page is then parsed and the requested information is extracted from the markup.</p>

                    <h3 className="text-2xl font-bold mt-10 my-2 text-headline">Security</h3>
                    <p>No user information is stored in any databases. All of the proccessing that happens in a request is dumped once the request has resolved.</p>

                    <h3 className="text-2xl font-bold mt-10 my-2 text-headline">Feedback</h3>
                    <p>If you have any feedback, please reach out to me at vs.nalavade2003@gmail.com</p>

                    <h3 className="text-2xl font-bold mt-10 my-2 text-headline">License</h3>
                    <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.
                </div>
            </div>
        </Layout>
    )
}

export default Home;