import React from 'react';

const Header = () => {
  return (
    <div>
      {/* Navigation Bar */}
      <nav className="navbar">
        <ul>
          <li><a href="">Home</a></li>
          <li><a href="/about/">About Us</a></li>
          <li><a href="/contact/">Contact Us</a></li>
          <li><a href="/ourwork/">Our Work</a></li>
          <li><a href="/auth/">Login/Signup</a></li>
          <li><a href="/event/">Book Event</a></li>
        </ul>
      </nav>

      {/* Header Image */}
      <header className="header">
        <img src="https://media.istockphoto.com/id/1188230341/photo/beautiful-decorative-colorful-roses-on-brick-wall.jpg?s=2048x2048&w=is&k=20&c=C38XJZN9-6WDfgdUr0i_gB6A6RduXjrdz3LhMQQzMzE=" alt="Wedding" style={{ filter: 'brightness(0.9)' }} />
        <div className="overlay">
          <div className="logo">
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Welcome to Vicky events <br />
            Let's Plan Your Fairytale Together !
          </div>
        </div>
      </header>

      {/* Services Section */}
      <div className="services-container">
        <br />
        <br />
        <h1>SERVICES WE PROVIDES</h1>
        <br />
        <br />

        <div className="services-grid">
          <div className="service-item">
            <a href="/destination/">
              <img src="https://plus.unsplash.com/premium_photo-1661964149725-fbf14eabd38c?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8ZGVzdGluYXRpb258ZW58MHx8MHx8fDA%3D" alt="Destination and Venues" />
            </a>
            <h2>DESTINATION</h2>
            <div className="overlay"></div>
          </div>

          {/* Add the rest of the service items here */}
        </div>
      </div>

      {/* Content Section */}
      <div className="content">
        <h1>Best Wedding Planner in Chandigarh</h1>
        <p>Putting all the beautiful pieces together and crafting one-of-a-kind experiences.</p>
        <br />
        <a href="/contact" className="vicky">Contact us</a>
      </div>
    </div>
  );
};

