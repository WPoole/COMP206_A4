#include<stdio.h>
#include<stdlib.h>
#include<string.h>

//Checks to see if user and correlating password exists
int findUsr(char* username, char* pass){
        FILE *fpr;
        fpr = fopen("users.txt", "rt");
        char line[300];
        fgets(line,299,fpr);
        if(feof(fpr)){
                return 1;
        }
        while(!feof(fpr)){
          char* token = strtok(line, "\n");
          if(strcmp(token, username)==0){
             fgets(line,299,fpr);
	     token = strtok(line, "\n");
		if(strcmp(pass,token)==0){
			return 0;
		}else{
			return 2;	
		}
	    
          }  
         fgets(line,299,fpr);
         fgets(line,299,fpr);
         fgets(line,299,fpr);
         fgets(line,299,fpr);
    
        }
        return 3;
}



int main(){

  char string[400];
  int n = atoi(getenv("CONTENT_LENGTH"));

  fgets(string,n+1,stdin);

        char* token = strtok(string, "=");
        char* username = strtok(NULL,"&");
        char* token2 = strtok(NULL,"=");
        char* pass = strtok(NULL, "\0");

	  //If user doesn't exists, redirect to login
          if(findUsr(username,pass)!=0){
                printf("Content-Type:text/html;charset=utf-8");
                printf("Content-Type:text/html\n\n");
                printf("");
                printf("<!DOCTYPE html>");
                printf("<html>");
                printf("<head>");
                printf("<title>Login and Registration</title>");
                printf("</head>");
                printf("<body>");
                printf("<h1><a href=login.html>Username or Password is incorrect!</a><h1>");
                printf("</body>");
                printf("</html>");
                return 0;
        }
	
	//If check user successful, continue to dashboard
	printf("Content-Type: text/html;charset=utf-8");
        printf("");
	printf("Content-Type:text/html\n\n");
        printf("<!DOCTYPE html>");
	printf("<html>");
        printf("<body>");
	printf("You logged in!");
	printf("</br>");
	printf("<form action=\"dashboard.py\" method=\"get\">");
	printf("<input type=\"hidden\" name=\"username\" value=%s>",username);
	printf("<input type=\"submit\" value=\"Continue to Dashboard\">");
	printf("</form>");
        printf("</body>");
        printf("</html>");
		
        return 0;
}
