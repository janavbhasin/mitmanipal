#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(int argc, char **argv)
{
	int r, s, l;
	MPI_Init(&argc, &argv);
	MPI_Comm_size(MPI_COMM_WORLD, &s);
	MPI_Comm_rank(MPI_COMM_WORLD, &r);
	char string[100], *str;
	if (r == 0)
    {
		printf("Enter string: ");
		fgets(string, sizeof(string), stdin);
		l = strlen(string);
		l /= s;
	}
    MPI_Bcast(&l, 1, MPI_INT, 0, MPI_COMM_WORLD);
	str = (char *)calloc(l, sizeof(char));
	MPI_Scatter(string, l, MPI_CHAR, str, l, MPI_CHAR, 0, MPI_COMM_WORLD);
	int c = 0;
	for (int i = 0; i < l; i++)
    {
		if (str[i]==' ' || str[i] == 'a' || str[i] == 'e' || str[i] == 'i' || str[i] == 'o' || str[i] == 'u' || str[i] == 'A' || str[i] == 'E' || str[i] == 'I' || str[i] == 'O' || str[i] == 'U')
        {
			c++;
        }
    }
    c=l-c;
    printf("Process %d has %d non-vowels\n",r,c);
	int *partial_counts = NULL;
    if (r == 0)
    {
        partial_counts = (int *)calloc(s, sizeof(int)); 
    }
    MPI_Gather(&c, 1, MPI_INT, partial_counts, 1, MPI_INT, 0, MPI_COMM_WORLD);  
    if (r == 0) 
    {
        int total_non_vowels = 0;
        for (int i = 0; i < s; i++) 
        {
            total_non_vowels += partial_counts[i];  
        }
        printf("The total non-vowels are: %d\n", total_non_vowels);
        free(partial_counts);
    }
    free(str);
    MPI_Finalize();
    return 0;
}