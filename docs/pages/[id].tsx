import React from "react";

export const getStaticPaths = async () => {
    const res = await fetch("https://jsonplaceholder.typicode.com/users");
    const data = await res.json();

    const paths = data.map((ninja : any) => {
        return {
            params: { id: ninja.id.toString() }
        }
    })

    return {
        paths,
        fallback: false
    }
}

export async function getStaticProps({ params }: { params: any }) {
    // params contains the post `id`.
    // If the route is like /posts/1, then params.id is 1
    const res = await fetch(`https://jsonplaceholder.typicode.com/users/${params.id}`)
    const post = await res.json()
  
    // Pass post data to the page via props
    return { props: { post } }
}

const Ninjas = ({ post }: { post: any }) => {
    return (
        <div>
            { post.name }
        </div>
    )
}

export default Ninjas;