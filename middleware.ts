import { NextRequest, NextResponse } from 'next/server'
import { Redis } from '@upstash/redis';
import { Ratelimit } from '@upstash/ratelimit'

const redis = Redis.fromEnv();
const ratelimit = new Ratelimit({
    redis: redis,
    limiter: Ratelimit.slidingWindow(5, '60 s')
})

export default async function middleware(request: NextRequest) {
    const ip = request.headers.get('x-forwarded-for')?.split(',')[0]?.trim()

    if (!ip) {
        return NextResponse.redirect(new URL('/blocked.html', request.url))
    }

    const { success, pending, limit, reset, remaining } = await ratelimit.limit(
        ip
    )

    return success
        ? NextResponse.next()
        : NextResponse.redirect(new URL('/blocked.html', request.url))
}

export const config = {
    matcher: ['/api/:path*'],
}