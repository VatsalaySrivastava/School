#!d:\Python34\python.exe
print("""
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Achievemts</title>
        <link href="css/bootstrap.css" rel="stylesheet">
        <link href="css/style.css" rel="stylesheet">
        <script src="js/jquery.js"></script>
        <script src="js/bootstrap.min.js"></script>
    </head>

    <body>
        <div class="navbar navbar-inverse navbar-fixed-top">
            <div class="container">
                <div class="navbar-header">
                    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>                        
                    </button>
                    <a class="navbar-brand" href="mains.py">College Achievements</a>
                </div>
                <div class="collapse navbar-collapse" id="myNavbar">
                    <ul class="nav navbar-nav navbar-right">
                        <li><a href="signup.py"><span class="glyphicon glyphicon-user"></span> Sign Up</a></li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="container" id="content">

            <!-- Jumbotron Header -->
            <div class="jumbotron home-spacer" id="products-jumbotron">
                <h1>TEACHER'S RECORD</h1>
                <p>JESSICA JOHNSON</p>

            </div>
            <hr>

            <div class="row text-center" id="cameras">
                <div class="col-md-3 col-sm-6 home-feature">
                    <div class="thumbnail">
                       <h3><u>THE TEACHER'S CV</u></h3>
                        <div class="caption">
                            <p>B.Sc in Chemistry from London University</p>
                            <p>M.Sc from Harvard University</p>
                            <p>Ph.D in Chemistry</p>
                           </div>
                    </div>
                </div>

                <div class="col-md-3 col-sm-6 home-feature">
                    <div class="thumbnail">
                        <h3><u>MORE ACHIEVEMENTS</u></h3>
                        <div class="caption">
                            <p>Worked with the renowned Medicine Pharmacy</p>
                            <p>Especiality in Organic Chemisrty</p>
                        </div>
                    </div>
                </div>

                <div class="col-md-3 col-sm-6 home-feature">
                    <div class="thumbnail">
                        <h3><u>CONTACT</u></h3>
                        <div class="caption">
                            <p>MOBILE NUMBER-9515203158,9110325413</p>
                            <p>E-MAIL-jjohnson121@gmail.com</p>
                        </div>
                    </div>
                </div>
            </div>
            <hr>
        </div>
        <footer>
            <div class="container">
                <center>
                    <p>Copyright &copy;College Achievements. All Rights Reserved  |  Contact Us: +91 94307 73356</p>	
                </center>
            </div>
        </footer>
    </body>
</html>
""")    
