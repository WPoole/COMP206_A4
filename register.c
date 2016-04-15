#include<stdio.h>
#include<stdlib.h>
#include<string.h>

//Function to add user into users.txt
void addUsr(char *username, char *pass, char *fullName, char *jobDesc){
	FILE *fp;
        fp = fopen("users.txt","a+");
        fprintf(fp, username);
        fprintf(fp, "\n");
        fprintf(fp, pass);
        fprintf(fp, "\n");
	fprintf(fp, fullName);
	fprintf(fp, "\n");
	fprintf(fp, jobDesc);
	fprintf(fp, "\n");

	FILE *friends;
	friends = fopen("friends.txt","a+");
	fprintf(friends, username);
	fprintf(friends, " \n");
}
//Returns 1 if user exists 0 if it doesn't
int checkUsr(char* username){
	FILE *fpr;
	fpr = fopen("users.txt", "rt");
	char line[300];
	fgets(line,299,fpr);
	if(feof(fpr)){
		return 0;
	}
	while(!feof(fpr)){
          char* token = strtok(line, "\n");
          if(strcmp(token, username)==0){
            return 1;
          }
         fgets(line,299,fpr);
	 fgets(line,299,fpr);
	 fgets(line,299,fpr);
	 fgets(line,299,fpr);

        }
        return 0;
}

int main(){

	char string[400];
  	int n = atoi(getenv("CONTENT_LENGTH"));

  	fgets(string,n+1,stdin);
	
	//Decodes string stored in stdin
	char* token = strtok(string, "=");
	char* username = strtok(NULL,"&");
	char* token2 = strtok(NULL,"=");
	char* pass = strtok(NULL, "&");
	char* token3 = strtok(NULL, "=");
	char* confPass = strtok(NULL, "&");
	char* token4 = strtok(NULL, "=");
	char* fullName = strtok(NULL, "&");
	char* token5 = strtok(NULL, "=");
	char* jobDesc = strtok(NULL, "\0");
	
	//Check to see if both fullName and jobDesc are empty or if fullName is filled and jobDesc is empty
	if(strncmp(fullName,"jobdesc",7)==0){
		printf("Content-Type: text/html;charset=utf-8");
                printf("Content-Type:text/html\n\n");
                printf("");
                printf("<!DOCTYPE html>");
                printf("<html>");
                printf("<head>");
                printf("<title>Login and Registration</title>");
                printf("</head>");
                printf("<body>");
                printf("<h1><a href=login.html>Please fill out each section!</a></h1>");
                printf("</body>");
                printf("</html>");
                return 0;
	}
		
	//Check to see if Full name is empty but jobDesc is filled
	if(jobDesc=='\0'){
		printf("Content-Type: text/html;charset=utf-8");
                printf("Content-Type:text/html\n\n");
                printf("");
                printf("<!DOCTYPE html>");
                printf("<html>");
                printf("<head>");
                printf("<title>Login and Registration</title>");
                printf("</head>");
                printf("<body>");
                printf("<h1><a href=login.html>Please fill out each section!</a></h1>");
                printf("</body>");
                printf("</html>");
                return 0;
	}

	//Check to see if passwords match
	if(strcmp(pass,confPass)!=0){
		printf("Content-Type: text/html;charset=utf-8");
        	printf("Content-Type:text/html\n\n");
		printf("");
		printf("<!DOCTYPE html>");
		printf("<html>");
		printf("<head>");
		printf("<title>Login and Registration</title>");
		printf("</head>");
		printf("<body>");
		printf("<h1><a href=login.html>Passwords do not match</a></h1>");
		printf("</body>");
		printf("</html>");
		return 0;
	}
	
	//Check to see if username is taken
	if(checkUsr(username)){
                printf("Content-Type: text/html;charset=utf-8");
		printf("Content-Type:text/html\n\n");
		printf("");
		printf("<!DOCTYPE html>");
		printf("<html>");
		printf("<head>");
		printf("<title>Login and Registration</title>");
		printf("</head>");
		printf("<body>");
		printf("<h1><a href=index.html>Username is taken</a><h1>");
		printf("</body>");
		printf("</html>");
		return 0;
	}

	printf("Content-Type: text/html;charset=utf-8");
	printf("");
	printf("Content-Type:text/html\n\n");
	printf("<html>");
	printf("<body>");
	printf("<h1><a href=\"login.html\">Success! Return to Login</a></h1>");
	printf("</body>");
	printf("</html>");

	addUsr(username, pass, fullName, jobDesc);

	return 1;
}
