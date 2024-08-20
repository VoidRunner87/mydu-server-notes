# MyDU Server Notes

## PVP

### PVPConfig Changes

For PVP Servers

```yaml
  planetsAreSafeZones: false
  safeZones:
  - centerX: 0
    centerY: 0
    centerZ: 0
    radius: 0
  planetProperties:
  - planetName: Madis Moon 3
    atmosphericRadius: 500000
  - planetName: Alioth
    atmosphericRadius: 0
```

### FeaturesList Changes

To Allow Base Shields on Static Cores

```yaml
  allowBaseShieldOnStaticConstruct: true
```

### Radars

If you remove atmosphere on planets and want the atmo radar to work.
There are two atmospheres: One is PVP Safe Zone and the other is the planetary

```yaml
RadarPvPAtmospheric:
 parent: RadarPVPUnit
 displayName: Atmospheric Radar
 description: Atmospheric Radars are appropriate for use within the influence of planets.
 scanRange: 10000
 worksInAtmosphere: false
 worksInSpace: true
```

## Cores

XL Static core 

```yaml
CoreUnitStatic512:
 parent: CoreUnitStatic
 constructSize: 512
 displayName: Static Core Unit 256m
 cellSize: 0.5
 hidden: false
 hitpoints: 50
```

## Industry, Market and Others

To Allow Industry on Dynamics or markets on dynamics:

Change FeaturesList:

```yaml
  allowIndustryOnDynamicConstruct: true
  allowMarketOnDynamicConstruct: true
```
