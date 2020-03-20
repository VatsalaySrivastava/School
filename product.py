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
                <h1>The Achievement Section!</h1>
                <p>We have the best achivement by the teachers and the students for our college and the research paper by the students.</p>

            </div>
            <hr>

            <div class="row text-center" id="cameras">
                <div class="col-md-3 col-sm-6 home-feature">
                    <div class="thumbnail">
                        <img src="img/t1.jpg" alt="">
                        <div class="caption">
                            <a href="teacher.py"><h3>Dr.Jessica Johnson</h3></a>
                            <p>Exellence in Chemistry</p>
                           </div>
                    </div>
                </div>

                <div class="col-md-3 col-sm-6 home-feature">
                    <div class="thumbnail">
                        <img src="img/t2.jpg" alt="">
                        <div class="caption">
                            <h3>Dr.David Bechmann</h3>
                            <p>Ph.D in Calculus </p>
                        </div>
                    </div>
                </div>

                <div class="col-md-3 col-sm-6 home-feature">
                    <div class="thumbnail">
                        <img src="img/t3.jpeg" alt="">
                        <div class="caption">
                            <h3>Dr.Priya Rai</h3>
                            <p>Social Worker</p>
                        </div>
                    </div>
                </div>

                <div class="col-md-3 col-sm-6 home-feature">
                    <div class="thumbnail">
                        <img src="img/t4.jpg" alt="">
                        <div class="caption">
                            <h3>Dr.Pramod Agarwal</h3>
                            <p>Ph.D in Statisitc</p>
                        </div>
                    </div>
                </div>
            </div>

            <div class="row text-center" id="watches">
                <div class="col-md-3 col-sm-6 home-feature">
                    <div class="thumbnail">
                        <img src="img/s1.jpg" alt="">
                        <div class="caption">
                            <h3>Adam Milne</h3>
                            <p>Topped the college</p>
                        </div>
                    </div>
                </div>

                <div class="col-md-3 col-sm-6 home-feature">
                    <div class="thumbnail">
                        <img src="img/s2.jpg" alt="">
                        <div class="caption">
                            <h3>Kristina Jeniffer</h3>
                            <p>Created online library for college</p>
                        </div>
                    </div>
                </div>

                <div class="col-md-3 col-sm-6 home-feature">
                    <div class="thumbnail">
                        <img src="img/s3.jpg" alt="">
                        <div class="caption">
                            <h3>Micheal Milan</h3>
                            <p>One credit cared for students for all purpose</p>
                        </div>
                    </div>
                </div>

                <div class="col-md-3 col-sm-6 home-feature">
                    <div class="thumbnail">
                        <img src="img/s4.jpg" alt="">
                        <div class="caption">
                            <h3>Sophia Hayat</h3>
                            <p>Created digital system for attendance</p>
                        </div>
                    </div>
                </div>
            </div>

            <div class="row text-center" id="shirts">
                <div class="col-md-3 col-sm-6 home-feature">
                    <div class="thumbnail">
                        <img src="img/r1.jpg" alt="">
                        <div class="caption">
                            <h3>Grammer Research</h3>
                            <p>By 1st Year</p>
                        </div>
                    </div>
                </div>

                <div class="col-md-3 col-sm-6 home-feature">
                    <div class="thumbnail">
                        <img src="img/r2.jpg" alt="">
                        <div class="caption">
                            <h3>Accounting Sheet</h3>
                            <p>By B.B.A</p>
                        </div>
                    </div>
                </div>

                <div class="col-md-3 col-sm-6 home-feature">
                    <div class="thumbnail">
                        <img src="img/r3.jpg" alt="">
                        <div class="caption">
                            <h3>Calculus Research</h3>
                            <p>By 3rd year</p>
                       </div>
                    </div>
                </div>

                <div class="col-md-3 col-sm-6 home-feature">
                    <div class="thumbnail">
                        <img src="img/r4.jpg" alt="">
                        <div class="caption">
                            <h3>Statical Research</h3>
                            <p>By 3rd year</p>
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
