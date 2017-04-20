open GL
open Glut

let display () =
  glClear [GL_COLOR_BUFFER_BIT];
  glColor3 ~r:1.0 ~g:0. ~b:0.;
  glBegin GL_TRIANGLES;
    glVertex2 (-1.0) (-1.0);
    glVertex2 ( 0.0) ( 1.0);
    glVertex2 ( 1.0) (-1.0);
  glEnd ();
  glFlush ()


let () =
  ignore(glutInit Sys.argv);
  glutInitDisplayMode [GLUT_SINGLE];
  ignore(glutCreateWindow ~title:"simple demo");
  glutDisplayFunc ~display;
  glutMainLoop ()
