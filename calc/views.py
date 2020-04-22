from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from calc.models import Teachers,addcourse,classroom,timetable
from collections import defaultdict
import psycopg2
import typing
from collections import defaultdict
'''from .models import User
from django.views.decorators.csrf import csrf_protect'''
# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html') 
def AddCourse(request):
    if request.method == 'POST':
        coursename=request.POST['courseName']
        subject1=request.POST['subject1']
        subject2=request.POST['subject2'] 
        subject3=request.POST['subject3']
        subject4=request.POST['subject4']
        teacher1=request.POST['subject1Teacher']
        teacher2=request.POST['subject2Teacher']
        teacher3=request.POST['subject3Teacher']
        teacher4=request.POST['subject4Teacher']
        
        course_info = addcourse(coursename=coursename,subject1=subject1,
        subject2=subject2,subject3=subject3,subject4=subject4,
        teacher1=teacher1,teacher2=teacher2,teacher3=teacher3,
        teacher4=teacher4)
        course_info.save()
        print('Course saved.')
        return redirect('add_course')
    else:
        return render(request,'AddCourse.html')  
 
def AddTeachers(request):
    if request.method == 'POST':
        teacherId=request.POST['teacherId']
        teacherName=request.POST['teacherName']
        teacherPhone=request.POST['teacherPhone']
        teacherEmailId=request.POST['teacherEmailId']

        if Teachers.objects.filter(teacherId=teacherId).exists():
            messages.info(request,'Id already exits')
            return redirect('add_teachers')
        elif Teachers.objects.filter(teacherEmailId=teacherEmailId).exists():
            messages.info(request,'Email taken')
            return redirect('add_teachers')
        else:
            '''user = User.objects.create_user(teacherId=teacherId,teacherName=teacherName,teacherPhone=teacherPhone,teacherEmailId=teacherEmailId)
            user.save();'''
            teachers_info = Teachers(teacherId=teacherId,teacherName=teacherName,teacherPhone=teacherPhone,teacherEmailId=teacherEmailId)
            teachers_info.save()
            print('Teacher saved.')
            return redirect('add_teachers')
    else:
        return render(request,'AddTeacher.html')  
def AddClassroom(request):
    if request.method == 'POST':
        room1 = request.POST['room1']
        room2 = request.POST['room2']
        room3 = request.POST['room3']
        room4 = request.POST['room4']
        classroom_info = classroom(room1=room1,room2=room2,room3=room3,room4=room4)
        classroom_info.save()
        print('Classrooms saved.')
        return redirect('class_room')
    else:
        return render(request,'classroom.html')
def createtimetable(request):
    if request.method == 'POST':
        info1 = timetable.objects.all()[24:48:6]
        info2 = timetable.objects.all()[25:48:6]
        info3 = timetable.objects.all()[26:48:6]
        info4 = timetable.objects.all()[27:48:6]
        info5 = timetable.objects.all()[28:48:6]
        info6 = timetable.objects.all()[29:48:6]

        #print(info)
        data = { "details1" : info1,"details2" : info2,"details3" : info3,"details4" : info4,"details5" : info5,"details6" : info6}
        #print(data)
        resp =  render(request,"display.html", data)
        return resp
    else:
        return render(request,'CreateTimeTable.html')  

def fetchData(request):
    if request.method == 'POST':        
        try:
            connection = psycopg2.connect(user="postgres",
                                            password="1234",
                                            host="localhost",
                                            port="5432",
                                            database="firstproject")
            cursor = connection.cursor()
            postgreSQL_select_Query = "select * from calc_addcourse where id in(select MAX(id) from calc_addcourse)"
  
            cursor.execute(postgreSQL_select_Query)
            print("Selecting rows from calc_teachers table using cursor.fetchall")
            teacher_records = cursor.fetchall()

            COLORS = [{"":""}]
            #for i in range (2,6):
            for col in teacher_records:
                COLORS.append({col[6]:col[2]})
                COLORS.append({col[7]:col[3]})
                COLORS.append({col[8]:col[4]})
                COLORS.append({col[9]:col[5]})
        
            
        

        
                graph = defaultdict(list) # type: typing.DefaultDict[list,list]
                edges = []

                def addEdge(graph,u,v):
                    graph[u].append(v)

                # definition of function
                def generate_edges(graph):

                    # for each node in graph
                    for node in graph:

                        # for each neighbour node of a single node
                        for neighbour in graph[node]:

                            # if edge exists then append
                            edges.append((node, neighbour))
                    return edges
                #for classrooms
                #COLORS = ["", {{info.teacher1}}, "tech2", "tech3", "tech4"]
                print(COLORS)

                # declaration of graph as dictionary
                addEdge(graph,'seca','secb')
                addEdge(graph,'seca','secc')
                addEdge(graph,'seca','secd')
                addEdge(graph,'secb','secc')
                addEdge(graph,'secb','secd')
                addEdge(graph,'secc','secd')



                # Driver Function call
                # to print generated graph
                print(generate_edges(graph))

                def isSafe(graph,color, v, c):

                    for u in range(0,N):
                        if (color[u] == c):
                            return False

                    return True



                def kColorable(graph, color, k, v, N):
                    teachers=[]
                    subjects=[]
                    if(v==N):
                        for v in range(0,N):
                            for x,y in COLORS[color[v]].items():
                                teachers.append(x)
                                subjects.append(y)

                        data1=teachers[0]+":"+subjects[0]
                        data2=teachers[1]+":"+subjects[1]
                        data3=teachers[2]+":"+subjects[2]
                        data4=teachers[3]+":"+subjects[3]

                        query = "INSERT INTO calc_timetable (section1,section2,section3,section4) VALUES (%s, %s, %s, %s)"
                        data = (data1,data2,data3,data4)

                        cursor.execute(query, data)
                        connection.commit()
                        print(teachers)
                        print(subjects)
                        #print()
                        #print("--------------------------------------------------------------------------------")
                        return

                    for c in range(1,k+1):
                        if (isSafe(graph, color, v, c)):

                            color[v] = c


                            kColorable(graph, color, k, v + 1, N)


                            color[v] = 0

                N=4
                k=4
                color=[0]*N
                kColorable(graph, color, k, 0, N)
                print("Print each row and it's columns values")
                

        except (Exception, psycopg2.Error) as error :
            print ("Error while fetching data from PostgreSQL", error)

        finally:
            #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")
        return redirect('fetchdata')
    else:
        return render(request,'CreateTimeTable.html')










''''class TeachersView(TemplateView):
    template_name = 'AddTeacher.html'

    def get(self, request):
        form = TeachersForm()
        return render(request, self.template_name, {'form': form})'''
