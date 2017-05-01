#include <stdio.h>
#define N 5
int m(int a[],int n){
	int i;
	int imax=a[0];
	for(i=0;i<n;i++){
		if(a[i]>imax) imax=a[i];
	}
	return imax;
	
}
int jc(int n){
	int i;
	int fa=1;
	for(i=1;i<=n;i++){
		fa=fa*i;
	}
	return fa;

}
int main(){
	int i,max,a[]={2,6,-3,5,7};
	max=a[0];
	for(i=0;i<N;i++){
		if(a[i]>max) max=a[i];
	}
	printf("%d\n",max);

	printf("%d\n",m(a,5));
	printf("%d\n",jc(5));
	return 0;
}