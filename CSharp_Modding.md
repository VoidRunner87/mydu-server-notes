# C# Modding

## Project Setup

* Create a Solution for the Project `Examples`
* Add to the `.csproj` the missing Nuget `<PackageReference>s`
  * `<PackageReference Include="YamlDotNet" Version="12.0.0" />`
  * `<PackageReference Include="Serilog" Version="2.0.0" />`
  * `<PackageReference Include="Microsoft.Orleans.Clustering.AdoNet" Version="3.6.5" />`
  * `<PackageReference Include="StackExchange.Redis" Version="2.0.601" />`
  * `<PackageReference Include="Grpc.Core" Version="2.40.0" />`
  * `<PackageReference Include="Microsoft.Toolkit.HighPerformance" Version="7.1.0" />`
  * `<PackageReference Include="InfluxDB.LineProtocol" Version="1.1.1" />`
  * `<PackageReference Include="MathNet.Spatial" Version="0.6.0" />`
* If you're going to run first locally on Windows:
  * Change the value of RUNTIME_ID in the file `Directory.Build.props`
    * `<RUNTIME_ID Condition="'$(RUNTIME_ID)' == ''">win-x64</RUNTIME_ID>`
* Copy the Missing DLLs from NQ from the Orleans Container
  * `docker cp CONTAINER_ID:/OrleansGrains D:\mydu-server\OrleansGrains`
    * CONTAINER_ID should be your container id
      * `docker ps` to see the container list - copy the id of the `dual-server-orleans`
      * `D:\mydu-server\` the path of the mydu-server folder you have on your machine
     
## Ports for Local Development

* Add port `30000` to the `orleans` container
  * By modifying the `docker-compose.yml` file
```yaml
  orleans:
    image: ${NQREPO}dual-server-orleans:$NQVERSION
    command: /config/dual.yaml
    volumes:
      - ${CONFPATH}:/config
      - ${DATAPATH}:/data
      - ${LOGPATH}:/logs
      - ./Mods:/OrleansGrains/Mods
    restart: always
    networks:
      vpcbr:
        ipv4_address: 10.5.0.13
    ports:
      - "30000:30000" # <-- Add PORT HERE
```
* Delete existing Docker Stack and Redeploy the Stack using the `up.bat` or `up.sh` script
   
## Documentation

* Read the documentation in the `mydu-mod-toolkit` folder - file: `mods-documentation.pdf`

## Run the Code Locally
