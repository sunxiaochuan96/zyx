#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

//选择排序
void SelectSort(vector<int> &v) {
	int n = v.size();
	for (int i = 0; i < n; i++) {
		int min = i;
		for (int j = i+1; j < n; j++) {
			if (v[j] < v[min]) {
				min = j;
			}
		}
		swap(v[i], v[min]);
	}
}

//冒泡排序
void BubbleSort(vector<int> &v) {
	int n = v.size();
	for (int i = 0; i < n; i++) {
		for (int j = i + 1; j < n; j++) {
			if (v[j] < v[i]) {
				swap(v[i], v[j]);
			}
		}
	}
}

//插入排序
void InsertSort(vector<int> &v, int n) {
	for (int i = 1; i < n; i++) {
		int temp = v[i];
		int j = i - 1;
		while (j >= 0 && v[j] > temp) {
			v[j + 1] = v[j];
			j--;
		}
		v[j + 1] = temp;
	}
}

//TOP k[桶排序]
vector<int> topKFrequent(vector<int> &v, int k) {
	int n = v.size();
	map<int, int> m;
	int max_count = 0;
	for (int i = 0; i < n; i++) {
		max_count = max(max_count, ++m[v[i]]);
	}

	vector<vector<int>> bucket(max_count + 1);
	for (auto i : m) {
		bucket[i.second].push_back(i.first);
	}
	
	vector<int> res;
	for (int i = max_count; i > 0 && res.size() < k; i--) {
		for (auto j : bucket[i]) {
			res.push_back(j);
			if (res.size() == k) {
				break;
			}
		}
	}
	return res;
}

//快速排序
void QuickSort(vector<int> &v, int start, int end) {
	if (start >= end) {
		return;
	}
	int pivot = start;
	int j = start + 1;
	for (int i = start + 1; i < end + 1; i++) {
		if (v[i] <= v[pivot]) {
			swap(v[i], v[j]);
			j++;
		}  
	}
	swap(v[pivot], v[j - 1]);
	pivot = j - 1;
	QuickSort(v, start, pivot - 1);
	QuickSort(v, pivot + 1, end);
}

//归并排序
void merge(vector<int> &v, vector<int> &temp, int start, int mid, int end) {
	// 左半区第一个未排序的元素
	int l = start;
	// 右半区第一个未排序的元素
	int r = mid + 1;
	// 临时数组下标
	int k = start;

	//合并
	while (l <= mid && r <= end) {
		if (v[l] <= v[r]) {  //左半区第一个剩余元素更小
			temp[k++] = v[l++];
		}
		else {	//左半区第一个剩余元素更小
			temp[k++] = v[r++];
		}
	}
	
	//合并左半区剩余元素
	while (l <= mid) {
		temp[k++] = v[l++];
	}

	//合并右半区剩余元素
	while (r <= end) {
		temp[k++] = v[r++];
	}

	//临时数组中的合并后元素复制到原来的数组
	while (start <= end) {
		v[start] = temp[start];
		start++;
	}

}
void MergeSort(vector<int> &v, vector<int> &temp, int start, int end) {
	if (start >= end) {
		return;
	}
	int mid = (start + end) / 2;
	MergeSort(v, temp, start, mid);
	MergeSort(v, temp, mid + 1, end);
	merge(v, temp, start, mid, end);
}


void printvector(vector<int>&v) {
	for (int i = 0; i < v.size(); i++) {
		cout << v[i] << " ";
	}
	cout << endl;
}


void main() {
	vector<int> v = { 9,11,13,4,6,5,7,12,1,10,2,8,8,16,16 };
	//SelectSort(v);
	//BubbleSort(v);
	//InsertSort(v);
	QuickSort(v, 0, v.size()-1);
	vector<int> temp(v.size());
	//MergeSort(v, temp, 0, v.size()-1);
	//vector<int> p = topk(v, 2);

	printvector(v);
	//printvector(p);
}


