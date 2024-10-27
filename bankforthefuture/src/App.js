import logo from './images/logo.svg';
import pic from './images/pic01.jpg';
import './App.css';
import { useState } from 'react';
import './assets/css/main.css'
import './assets/css/noscript.css'

function App() {
  const [mInc, setMInc] = useState();
  const [mExp, setMExp] = useState();

  console.log(mInc, ' ', mExp);

  const url = 'http://127.0.0.1:5000/'
  async function handleSubmit() {
    const result = await fetch(url,
    {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ mInc, mExp })
    })

    const data = await result.json();
    console.log(data);
    if(result.status !== 200) {
      console.error('Request Failed')
      return;
    }
    console.log(JSON.stringify(data.users, null, 2));
    }

  return (
    <div className="App">
	<head>
		<title>HackForTheFuture</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
	</head>
	<body class="is-preload">


			<div id="wrapper">


					<header id="header" class="alt">
						<span class="logo"><img src={logo} alt="" /></span>
						<h1>BankForTheFuture</h1>
						<p>We're here to help the unbanked, get banked<br />
						built by <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ">@UTSAGIRLS</a> for ROWDYHACKS X.</p>
					</header>


					<nav id="nav">
						<ul>
              <li><a href="#cta">START HERE</a></li>
							<li><a href="#intro" class="active">About</a></li>
						</ul>
					</nav>


					<div id="main">

            <section id="cta" class="main special">
              <header class="major">
                <h2>Get Started HERE!!!</h2>
              </header>
              <body>
                <form action="{{ url_for('/') }}" method="post">
                  <label for="fname">Estimated Monthly Income:</label>
                  <input type="text" id="mInc" name="mInc" value={mInc} onChange={(e) => setMInc(e.target.value)} style={{width: '300px', display: 'block', margin: '0 auto'}}/><br/>
                  <label for="lname">Estimated Monthly Expenses:</label>
                  <input type="text" id="mExp" name="mExp" value={mExp} onChange={(e) => setMExp(e.target.value)} style={{width: '300px', display: 'block', margin: '0 auto'}}/><br/>
				          <button id="mybutton">Submit</button>
                </form>
                
                <p>If you click the "Submit" button, the form-data will be sent to a page called "/action_page.php".</p>
                
                </body>
            </section>


							<section id="intro" class="main">
								<div class="spotlight">
									<div class="content">
										<header class="major">
											<h2>About Us!</h2>
										</header>
										<p>At HackForTheFuture, we’re dedicated to making financial planning accessible and straightforward 
                      for everyone. Our program is designed to simplify complex financial concepts, allowing users to easily 
                      input their financial information without needing a deep understanding of intricate calculations or 
                      economic jargon. We transform this data into clear, attractive visuals that help you see your financial 
                      future at a glance. Whether you're planning for major life goals or just want to get a better handle on 
                      your finances, our mission is to provide a user-friendly, visually intuitive tool to guide you every step 
                      of the way. Empowering you to make informed financial decisions has never been easier!</p>
										{/* </ul> */}
									</div>
									<span class="image"><img src={pic} alt="" /></span>
								</div>
							</section>
							<section id="first" class="main special">
								<header class="major">
									<h2>What do we use?!</h2>
								</header>
								<ul class="features">
									<li>
										<span class="icon solid major style1 fa-code"></span>
										<h3>Coding languages</h3>
										<p>For this project, we used Python, React, Flask, and JS!</p>
									</li>
								</ul>
								<footer class="major">
									{/* </ul> */}
								</footer>
							</section>
					</div>
					<footer id="footer">
						<p class="copyright">&copy; UTSAGIRLS. Design: <a href="https://html5up.net">HTML5 UP</a>.</p>
					</footer>
			</div>
			{/* <script src="assets/js/jquery.min.js"></script>
			<script src="assets/js/jquery.scrollex.min.js"></script>
			<script src="assets/js/jquery.scrolly.min.js"></script>
			<script src="assets/js/browser.min.js"></script>
			<script src="assets/js/breakpoints.min.js"></script>
			<script src="assets/js/util.js"></script>
			<script src="assets/js/main.js"></script> */}
      <button onClick={handleSubmit}>BUTTON</button>
	</body>

      
    </div>
  );
}

export default App;