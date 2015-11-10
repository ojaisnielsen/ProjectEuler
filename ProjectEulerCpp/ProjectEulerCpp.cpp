// ProjectEulerCpp.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


int main()
{
	__int64 b = 2;
	__int64 n = 2;
	__int64 s_b = 2;
	__int64 s_n = 1;
	while (n < 1000000000000)
	{
		do
		{
			if (s_b < s_n)
			{
				s_b += 2 * b++;
			}
			else
			{
				s_n += n++;
			}
		} while (s_b != s_n);
		printf("%I64d, %I64d\n", b, n);
	}

}

