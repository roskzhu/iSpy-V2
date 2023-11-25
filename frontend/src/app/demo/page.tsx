import React from 'react'
import Link from 'next/link'
import NavBar from '@/app/components/navbar'
import Footer from '@/app/components/footer'
import '@/app/styles/demo.css'

const demo = () => {
  return (
    <div>
        <NavBar />
        <div className="screen">
            <div className="camera-wrapper">
                <div className="webcam"></div>
            </div>
        </div>
        <Footer />
    </div>
  )
}

export default demo

