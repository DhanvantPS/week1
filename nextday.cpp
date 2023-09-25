#include <stdio.h>

int main() {
int yr,mth,day;
scanf("%d %d %d",&day,&mth,&yr);
    if (mth==4 || mth==6  || mth==9  || mth==11)
    {
        if (day==30)
        {
            printf("%d %d %d",1,mth+1,yr);
        }
        else if(day>=1 && day<30)
        {
            printf("%d %d %d",day+1,mth,yr);
        }
        else
        {
            printf("invalid input");
        }
    }
    else if(mth==2 && (yr%4==0 && (yr%400==0 || yr%100!=0)))
    {
        if (day==29)
        {
            printf("%d %d %d",1,mth+1,yr);
        }
        else if(day>=1 && day<29)
        {
            printf("%d %d %d",day+1,mth,yr);
        }
        else
        {
            printf("invalid input");
        }
    }
    else if(mth==2)
    {
        if (day==28)
        {
            printf("%d %d %d",1,mth+1,yr);
        }
        else if(day>=1 && day<28)
        {
            printf("%d %d %d",day+1,mth,yr);
        }
        else
        {
            printf("invalid input");
        }
    }
    else if (mth==1 || mth==3 || mth==5 || mth==7 || mth==8 || mth==10)
    {
        if (day==31)
        {
            printf("%d %d %d",1,mth+1,yr);
        }
        else if(day>=1 && day<31)
        {
            printf("%d %d %d",day+1,mth,yr);
        }
        else
        {
            printf("invalid input");
        }
    }
    else if(mth==12)
    {
        if (day==31)
        {
            printf("%d %d %d",1,1,yr+1);
        }
        else if(day>=1 && day<31)
        {
            printf("%d %d %d",day+1,mth,yr);
        }
        else
        {
            printf("invalid input");
        }
    }
    
}