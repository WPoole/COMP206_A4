#include<stdio.h>
#include<stdlib.h>
#include<string.h>

// FUNCTION TO GET FIRST WORD OF STRING
void getFirstWord(char *input, char *output) {
  int i = 0;
  while(input[i] != ' ' && input[i] != '\n' && input[i] != '\0') {
    output[i] = input[i];
    i++;
  }
  output[i] = '\0';
}

int isWhiteSpace(char *string) {
  int i = 0;
  while(string[i] != '\n' && string[i] != '\0') {
    if(string[i] != ' ')
      return 0;
    i++;
  }
  return 1;
}


int main(){

  printf("Content-Type: text/html;charset=utf-8");
  printf("");
  char *filepath = "friends.txt";
  FILE *file_ptr;
  char line[300];
  char firstUsername[300];

  file_ptr = fopen(filepath, "rt");
  fgets(line, 299, file_ptr);
  getFirstWord(line, firstUsername);
  printf("%s\n", firstUsername);
  if(!strcmp(firstUsername, "flo")) {
    // DO NOTHING
  } else {

    while(!feof(file_ptr)) {
      // GET NEXT LINE.
      fgets(line, 299, file_ptr);
      getFirstWord(line, firstUsername);
      printf("Content-Type: text/html;charset=utf-8");
      printf("");
      printf("%s\n", firstUsername);
      if(!strcmp(firstUsername, "flo")) {
        break;
      }

    }
  }

  // NOW THAT WE HAVE THE LINE, JUST USE "strtok()" TO GET ALL REMAINING TOKENS.
  const char s[2] = " ";
  char *token;

  /* get the first token */
  token = strtok(line, s);
  // NEED THIS HERE TO AVOID PRINTING USERNAME OF CURRENT USER.
  token = strtok(NULL, s);




  printf("Content-Type:text/html\n\n");
  printf("<html>");
  printf("<head>");
  printf("<title>See A Friend</title>");
  printf("</head>");
  printf("<body>");
  printf("<h1>Welcome to your Personal Dashboard [INSERT USER'S NAME HERE]!</h1>");
  printf("<h3>Menu: </h3>");
  printf("<form action=\"welcome.html\">");
  printf("<button>Logout</button>");
  printf("</form>");
  printf("<form action=\"makefriends.py\">");
  printf("<button>Make a Friend</button>");
  printf("</form>");
  printf("<form action=\"seefriends.cgi\">");
  printf("<button>See a Friend</button>");
  printf("</form>");
  printf("<br>");
  printf("<br>");
  printf("<br>");

  int countPrintedUsernames = 0;
  printf("<form action=\"friendInfo2.py\" method=\"get\">");
  while( token != NULL )
  {
    if(!isWhiteSpace(token)){
      countPrintedUsernames ++;
      printf( "<input type=\"radio\" name=\"username\" value=\"%s\" checked> %s<br>", token, token );
    }

    token = strtok(NULL, s);
  }

  if(countPrintedUsernames != 0) {
    printf("<input type=\"submit\" value=\"See Profile\">");
  } else {
    printf("<h3>You don't have any friends yet! To be able to see your friends, please first add some friends, then try this page again.</h3>");
  }
  printf("</form>");


  printf("</body>");
  printf("</html>");

  return 1;
}

