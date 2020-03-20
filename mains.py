#!d:\Python34\python.exe
print("""
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Welcome To College Achievements</title>
        <!-- Bootstrap Core CSS -->
        <link href="css/bootstrap.css" rel="stylesheet">
        <!-- Custom CSS -->
        <link href="css/style.css" rel="stylesheet">
        <!-- jQuery -->
        <script src="js/jquery.js"></script>
        <!-- Bootstrap Core JavaScript -->
        <script src="js/bootstrap.min.js"></script>
    </head>

    <body style="padding-top: 50px;">
        <!-- Header -->
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
        <!--Header end-->

        <div id="content">
            <!--Main banner image-->
            <div id = "banner_image">
                <div class="container">	
                    <center>
                        <div id="banner_content">
                            <h1>We display honor</h1>
                            <br/>
                            <a  href="signup.py" class="btn btn-danger btn-lg active">SignUp Now</a>
                        </div>
                    </center>
                </div>
            </div>
            <!--Main banner image end-->
            <h3 align="center">NEWS FEED</h3>
 <marquee onmouseover="stop();" onmouseout="start();">COLLEGE EVENT:KHEL 2k19,SRM-MUN--19</marquee>
  <marquee onmouseover="stop();" onmouseout="start();">TCS INTERVIEW IS GOING ON IN THE MINI AUDITORIUM</marquee>
            <!--Item categories listing-->
            <div class="container">
                <div class="row text-center" id="item_list">
                    <div class="col-sm-4">
                        <a href="product.py#cameras" >
                            <div class="thumbnail">
                                <img src="img/1.jpg" alt="">
                                <div class="caption">
                                    <h3>Teacher's Achievement</h3>
                                    <p>The best of the Teacher's contribution.</p>
                                </div>
                            </div> 
                        </a>
                    </div>

                    <div class="col-sm-4">
                        <a href="product.py#watches" >
                            <div class="thumbnail">
                                <img src="img/100.jpg" alt="">
                                <div class="caption">
                                    <h3>Student's Achievement</h3>
                                    <p>The best of the Student's contribution.</p>
                                </div>
                            </div> 
                        </a>
                    </div>

                    <div class="col-sm-4">
                        <a href="product.py#shirts" >
                            <div class="thumbnail">
                                <img src="img/130.jpg" alt="">
                                <div class="caption">
                                    <h3>Research Papers</h3>
                                    <p>The best of the research papers.</p>
                                </div>
                            </div>
                        </a>
                    </div>
                </div>
            </div>
            <!--Item categories listing end-->
        </div>

        <!--Footer-->
        <footer>
            <div class="container">
                <center>
                    <p>Copyright &copy;College Achievements. All Rights Reserved  |  Contact Us: +91 94307 73356</p>	
                </center>
            </div>
        </footer>
        <!--Footer end-->

    </body> 
</html>
""")
