import psycopg2
import typing
from collections import defaultdict
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
        if(v==N):
            for v in range(0,N):
                print(COLORS[color[v]], end=" ")
            '''data1=COLORS[color[0]]
            data2=COLORS[color[1]]
            data3=COLORS[color[2]]
            data4=COLORS[color[3]]
            query = "INSERT INTO calc_timetable (data1,data2,data3,data4) VALUES (%s, %s, %s, %s);"
            data = (data1,data2,data3,data4)

            cursor.execute(query, data)'''
            print()
            print("--------------------------------------------------------------------------------")
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

#from calc.views import allTechSubInfo
# function for adding edge to graph
