from py4j.java_gateway import launch_gateway, JavaGateway

# where;s the ideal place to place the robor jar locally?
print("pre launch")
launch_gateway(jarpath='/usr/local/bin/robot.jar',
               classpath='org.obolibrary.robot.PythonOperation',
               port=25333,
               die_on_exit=True)
print("post launch, pre-gateway")
gateway = JavaGateway()
print("post gateway, pre-io_helper")
io_helper = gateway.jvm.org.obolibrary.robot.IOHelper()
print("post io_helper, pre-loadOntology")
ont = io_helper.loadOntology('/home/mark/git-repos/obi/obi.owl')
print("post loadOntology")
print(ont.getOntologyID().getVersionIRI())