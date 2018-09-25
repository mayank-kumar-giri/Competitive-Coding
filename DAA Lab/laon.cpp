#include <bits/stdc++.h>
using namespace std;

int main()
{

	int N;
	cin>>N;
	int arr[N];
	for(int i=0;i<N;i++) cin>>arr[i];

	map<int,pair<int,int> > M; //map the index of the array element with the pair of count and index that implies the element with the minimum index which is repeated
	map<int,pair<int,int> > ::iterator it;//iterator to traverse the map
	for(int i=0; i<N; i++)//select an element
		{
			it = M.find(arr[i]); //find the element

			if(it != M.end())//if element already present update its count
			{
				pair<int,pair<int,int> > temp = (*it);
				pair<int,int> p = temp.second;
				p.second++;
				M.erase(it);
				M.insert(make_pair(arr[i],p));
			}

			else //if element came for the first time then add it into the map with count 1 and occurence at i
			M.insert(make_pair(arr[i],make_pair(i,1)));
		}

	int min_index = INT_MAX; //obtaint the minimum index
	for(it = M.begin(); it != M.end(); it++) //traverse the entire map
		{
		pair<int,pair<int,int> > temp = (*it);
		pair<int,int> p = temp.second;
		if(p.second > 1)
			min_index = min(min_index,p.first);	//minimum index of the element that is repeating
		}

	if(min_index != INT_MAX)
	cout<<"First repeating element that is repeated is "<<arr[min_index];
	else
	cout<<"No repeating integer found\n";


}
