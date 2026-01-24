#This file will generate the quiz
from latexrender import *
import random
render = LatexRender() #This turns the input into LaTex.
from collections import Counter
counter=Counter()
#This function prepares the array to be displayed by the renderer
def display_array(arr, red=[], blue =[], underline = []):
    if len(arr)==0:
        return
    colors = ['red' if i in red else 'blue' if i in blue else None for i, elt in enumerate(arr)]
    underline = [True if i in underline else False for i, elt in enumerate(arr)]
    render.render(arr, color=colors, underline=underline)

'''Functions that you could be quizzed on. 
The following 5 functions could appear on the quiz.
They are identical to the implementations in the notes, except that the output is displayed in LaTex.
'''

def selection_sort(arr: list[int], quiet_mode: bool = True) -> None:
    '''
    Input: arr (a list of integers).
           quiet_mode (a boolean, whether or not to print intermediate steps)
    Output: None
    Side-Effects: mutates arr so that it is sorted.
    Repeatedly finds the smallest incorrectly-placed element and swaps it to the correct position.
    '''
    n= len(arr)
    for passnumber in range(n-1):
        if not quiet_mode:
            render.render(f"{passnumber=}")
        min_candidate = arr[passnumber]
        min_candidate_index = passnumber
        for i, candidate in enumerate(arr[passnumber+1:], start = passnumber+1): #This loop finds the smallest element after the first passnumber number of candidates.
            if not quiet_mode:
                display_array(arr, red = [i, min_candidate_index], underline = list(range(0,passnumber)))
            if min_candidate > candidate:
                min_candidate_index, min_candidate = i, candidate
        arr[passnumber], arr[min_candidate_index] = arr[min_candidate_index], arr[passnumber]
    if not quiet_mode:
        display_array(arr[:], underline = list(range(0,n-1)))

def insertion_sort(arr: list[int], quiet_mode: bool=True) -> None:
    '''
    Input: arr (a list of integers).
       quiet_mode (a boolean, whether or not to print intermediate steps)
    Output: None
    Side-Effects: mutates arr so that it is sorted.
    Repeatedly inserts the next element of arr into the sorted portion of the list.
    '''
    n = len(arr)
    for passnumber in range(n):
        current_index = passnumber
        if not quiet_mode:
            render.render(f"{passnumber=}")
            display_array(arr[:], red=[current_index, current_index-1], underline = list(range(0,passnumber)) )
        while current_index >0 and arr[current_index] < arr[current_index-1]:
            arr[current_index], arr[current_index-1] = arr[current_index-1], arr[current_index]
            current_index-=1
            if not quiet_mode:
                 display_array(arr[:], red = [current_index, current_index-1], underline = list(range(0,passnumber)) )

def merge_step(list1: list[int], 
               list2: list[int], 
               quiet_mode: bool = True) -> list[int]:
    '''
    Input:assumes list1 and list2 are sorted lists of integers
                quiet_mode is a boolean that indicates whether to print intermediate steps.
    Output: the list (list1+list2).sort()'''
    new_list=[]
    color_list = [] #used to color the outputs when quiet_mode is False.
    while(len(list1)>0 and len(list2)>0):
        #Iteratively move the smaller of the smallest to the new list until one list is empty.
        if not quiet_mode:
            render.render("lists to merge:")
            display_array(list1+list2, red = list(range(len(list1))), 
                        blue = list(range(len(list1),len(list1+list2) )) )
            render.render("new list:")
            display_array(new_list, 
                          red = [i for i,c in enumerate(color_list) if c == 'b'],
                          blue = [i for i,c in enumerate(color_list) if c == 'r'], 
                          underline = [len(new_list)-1])
        
        smallest_of_list1 = list1[0]
        smallest_of_list2 = list2[0]
        if smallest_of_list1<smallest_of_list2:
            list1=list1[1:] #Removes the first item of list1
            new_list.append(smallest_of_list1) #Puts that first item on new_list.
            color_list.append('b')
        else:
            list2 = list2[1:]
            new_list.append(smallest_of_list2)
            color_list.append('r')
    if not quiet_mode:
        display_array(new_list, 
                          red = [i for i,c in enumerate(color_list) if c == 'b'],
                          blue = [i for i,c in enumerate(color_list) if c == 'r'], 
                          underline = [len(new_list)-1])
    #At this point, at least one of list1 or list2 is empty. 
    #Put the remaining part of the nonempty list on the end of new_list.
    if len(list1)==0:
        new_list.extend(list2)
        color_list.extend(['r']*len(list2))
    elif len(list2)==0:
        new_list.extend(list1)
        color_list.extend(['b']*len(list1))
    if not quiet_mode:
        render.render("final combined sorted list")
        display_array(new_list, 
                          red = [i for i,c in enumerate(color_list) if c == 'b'],
                          blue = [i for i,c in enumerate(color_list) if c == 'r'])
    return new_list

def mergesort(list_to_sort: list[int], 
              quiet_mode: bool = True,
              id: int = 0,
              parent: int | None = None) -> list[int]:
    '''
    A divide-and-conquer method for sorting.
    Input: lists_to_sort is a list of integers. 
        quiet_mode is a flag that determines whether partial outputs will be printed.
        id is an integer that identifies this run of mergesort.
        parent is an integer that identifies the run of mergesort that called the current one.
    Output: a sorted version of list_to_sort
    Side-Effects: None
    '''
    if len(list_to_sort)<=1: #Base case.
        return list_to_sort
    if id==0:
        counter["merge_id"]=0
    counter["merge_id"]+=1
    #The divide step:
    middle = len(list_to_sort)//2 
    list1 = list_to_sort[:middle] 
    list2 = list_to_sort[middle:] 
    #Conquer, recursively:
    list1 = mergesort(list1, quiet_mode=quiet_mode, id=counter["merge_id"], parent = id)
    list2 = mergesort(list2, quiet_mode=quiet_mode, id=counter["merge_id"], parent = id)
    if not quiet_mode:
        render.render(f"{id=}, {parent=}")
        display_array(list1+list2, red = list(range(len(list1))), 
                                    blue = list(range(len(list1),len(list1+list2) )) )
        display_array(merge_step(list1,list2))
        render.render("---")
    #Complete conquering at this step by calling merge_step to combine the sorted lists, list1 and list2
    return merge_step(list1,list2)
def quicksort(arr: list[int], 
              quiet_mode: bool = False,
              id: int = 0,
              parent: int | None = None) -> list[int]: #Code initially generated by ChatGPT3.5
    '''
    Input: arr is an unsorted list.
            quiet_mode is a boolean that indicates whether to print additional information.
            id is an integer that identifies this particular call to quicksort.
            parent is an integer that is the id of the call to quicksort that called this one.
    Output: a sorted list.
    Side-Effects: None.
    Repeatedly selects a 'pivot' element. 
        Creates a new list with all elements less than the pivot to its left 
                            and elements greater than the pivot to its right.
        Then recurse on both the left and right parts of the list.
    '''
    
    if len(arr) <= 1:
        return arr
    if id==0:
        counter["quick_id"]=0
    counter["quick_id"]+=1

    pivot_index = len(arr) // 2
    pivot = arr[pivot_index] #Chooses the pivot to be in the middle.
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    if not quiet_mode:
        #We print the unsorted array with the pivot in bold.
        render.render(f"{id=},{parent=}")
        display_array(arr, 
                      underline = [pivot_index],
                    )
        #Then we print the array after moving the elements less than the pivot to its left and moving the elements greater than the pivot to its right.
        display_array(left + middle+right, blue = list(range(len(left))), 
                      underline = [len(left)],
                      red = list(range(len(left)+len(middle), len(arr)) ) )
        
        render.render('---')
    return (quicksort(left,
                     quiet_mode=quiet_mode,
                     id=counter["quick_id"],
                     parent = id) 
                     
            + middle 
            + quicksort(right,
                        quiet_mode=quiet_mode, 
                        id = counter["quick_id"], 
                        parent = id) #Makes two recursive calls.
    )

if __name__=='__main__':
    questions = random.sample([0,1,2,3,4], 2)
    arr = [random.randint(0,99) for _ in range(8)]
    if 0 in questions:
        render.render(r"SelectionSort")
        render.render('''Instructions: Fill in the missing steps
                        The active comparison is in red, before swapping. You should circle these numbers.
                        Numbers that have already been handled are underlined. You should underline these numbers.''')
        arr = [random.randint(0, 99) for _ in range(8)]
        render.render("initial array")
        display_array(arr)
        selection_sort(arr,quiet_mode=False)
        assert arr == sorted(arr)
    if 1 in questions:
        render.render(r"InsertionSort")
        render.render('''Instructions: Fill in the missing steps
                        The active comparison is in red, before swapping. You should circle these numbers.
                        Numbers that have already been handled are underlined. You should underline these numbers.''')
        arr = [random.randint(0, 99) for _ in range(8)]
        render.render("initial array")
        display_array(arr)
        insertion_sort(arr,quiet_mode=False)
        assert arr == sorted(arr)
    if 2 in questions:
        render.render(r"MergeStep")
        render.render('''Instructions: Fill in the missing steps
                        The first list is in red. You should circle these numbers.
                        The second list is in blue. You should box these numbers.
                        Numbers that have already been handled are underlined. You should underline these numbers.''')
        arr1 = sorted([random.randint(0, 99) for _ in range(5)])
        arr2 = sorted([random.randint(0, 99) for _ in range(5)])
        render.render("initial arrays")
        render.render("arr1")
        display_array(arr1)
        render.render("arr2")
        display_array(arr2)
        arr = merge_step(arr1,arr2,quiet_mode=False)
        assert arr == sorted(arr)
        counter.clear()
    if 3 in questions:
        render.render(r"MergeSort")
        render.render('''Instructions: Fill in the missing steps
                        The first list is in red. You should circle these numbers.
                        The second list is in blue. You should box these numbers.''')
        arr = [random.randint(0, 99) for _ in range(8)]
        render.render("initial array")
        display_array(arr)
        arr = mergesort(arr, quiet_mode=False)
        assert arr == sorted(arr)
        counter.clear()
    if 4 in questions:
        render.render(r"Quicksort")
        render.render(r'''Instructions: Fill in the missing steps.
                        The pivot will be bolded.
                        After moving numbers on either side of the pivot, numbers left of the pivot are colored blue. You should box these numbers.
                        The numbers on the right of the pivot are colored red. You should circle these numbers.''')
        arr = [random.randint(0, 99) for _ in range(8)]
        render.render("initial array")
        display_array(arr)
        arr = quicksort(arr, quiet_mode=False)
        assert arr == sorted(arr)
        counter.clear()

    render.to_latex('out.tex')