import type { NextPage } from 'next'

import Layout from '../components/layout'
import Footer from '../components/footer'

const Home: NextPage = () => {
  return (
    <Layout>
    <section>
        <div className='flex flex-col justify-center items-center'>
          <h1 className='text-7xl font-bold text-headline text-center'>Frisco ISD HAC API</h1>
          <h2 className='text-paragraph text-center'>REST API to retrieve data from HAC (Home Access Center)</h2>

          <span className='bg-highlight text-main py-2 px-14 mt-8 rounded-md hover:bg-headline-darker' >Get Started</span>
        </div>
    </section>

    <Footer />
    </Layout>
  )
}

export default Home
