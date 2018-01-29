#include<stdio.h>
int main()
{
	int T, n, m, c, x, y, i=0, j=0, count=0;
	scanf("%d", &T);
	if(T>=1 && T<=100)
	{
		for(i=0; i<T; i++)
		{
			
			scanf("%d %d %d", &n, &m, &c);
			if(n>=1 && n<=1000000 && m>=1 && m<=1000000 && c>=1 && c<=1000000)
			{
				if ((n*m)>=c)
				{
					for(j=1; (j*j)<c; j++)
					{	
						x=j;
						if(c%x==0)
							y=c/x;
						else
							continue;
						if(x<=m && y<=n)
							count++;
						if(x<=m && y<=m && x!=y)
							count++;
					}
					printf("%d\n", count);
				}
				else 
				{
					printf("0");
				}
			}
			
		}
		
	}
	return 0;
}
