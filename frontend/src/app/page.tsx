import Image from 'next/image'
import Link from 'next/link'
import NavBar from '@/app/components/navbar'
import Footer from '@/app/components/footer'
import '@/app/styles/home.css'

export default function Home() {
  return (
    <main>
      <NavBar />
      <video playsInline autoPlay muted loop>
        <source src="/video-bg.mp4" type='video/mp4'/>
      </video>
      <div className="home">
        <div className="landing-page">
          <div className="landing-left">
            <div className="ispy">iSpy</div>
            <div className="slogan"><i>iSpy with my little eye, protected communities and a safer tomorrow.</i></div>
            <div className="get-started"><Link href="#info"><button>Get Started</button></Link></div>
          </div>
          <div className="landing-right">
            <div className="landing-image"><Image src="/placeholder.jpg" alt='placeholder' width='400' height="200"></Image></div>
          </div>
        </div>
        <div id='info'></div>
        <div className="information-section">
          <div className="about">
            <div className="title">About</div>
            <div className="paragraph">
              Welcome to iSpy, the next frontier in <b><i>intelligent home security</i></b>. 
              Our cutting-edge software goes beyond traditional measures of employing face detection features. 
              Using advanced AI techniques and a customize-able database, we are able to classify individuals as homeowners, strangers, and additional labels. 
              What makes iSpy stand out is its incredible accuracy, low margin for error and ability to be tailored exclusively to your home. 
              We're here to help secure your world, <b><i>one face at a time</i></b>. 
              Feel free to try out our web demo following the guidelines below!
            </div>
            <div className="guide"><b>Quick Guide:</b></div>
            <ol>
              <li>1. <b><u>Upload</u>:</b> Take a short video screening of your face, supply a label, and take a quick break while we train the model.</li>
              <li>2. <b><u>Test</u>:</b> Done! The user is now added to the system for seamless recognition on your computer’s webcam.</li>
            </ol>
          </div>
          <div className="integration">
            <div className="subheader">Security Camera Integration</div>
            <div className="motto"><i>Personalized security, wherever you go.</i></div>
            <div className="product-demo">Product Demo</div>
            <div className="demo-attachment"><Image src="/placeholder.jpg" alt="placeholder" width="200" height="100"></Image></div>
            <div className="p1">Protecting young children from unwelcomed guests.  Identifying wanted criminals. Performing data collection on a building’s visitors. Monitoring individuals in your home.</div>
            <div className="p2"><b>iSpy does it all ... and more.</b></div>
            <div className="p3"><i>Tailor our software to support your needs and integrate it with your surveillance cameras for unmatched security.</i></div>
            <div className="learn-more"><Link href="https://github.com/roskzhu/iSpy-V2/tree/main"><button>Learn More</button></Link></div>
          </div>
        </div>
      </div>
      <Footer />
    </main>
  )
}
