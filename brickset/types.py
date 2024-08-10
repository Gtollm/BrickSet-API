# -*- coding: utf-8 -*-

from datetime import date
import re
from types import ClassMethodDescriptorType

class JsonDeserializable():
    """
 Subclasses of this class are guaranteed to be able to be created from a json formatted string.
    All subclasses of this class must override deJson.
    """

    def deJson(self, json_string):
        """
        Returns an instance of this class from the given json string.
        This function must be overridden by subclasses.
        """
        raise NotImplementedError

class ApiKeyUsage:
    """
    A class for keeping score of current API usage
    
    Attributes:
        dateStamp : date 
            date for apiKeyUsage
        count : int 
            number of spiKeyUsage
    """
    def __init__(self, dateStamp:date, count:int):
        """
        Initialization of apiKeyUsage class

        Args:
            dateStamp : date for apiKeyUsage
            count : number of spiKeyUsage
        """
        self.dateStamp = dateStamp
        self.count = count
    def __str__(self):
        """
        String interpretation of apiKeyUsage class

        Returns:
            str : apiKeyUsage data with a space in between    
        """
        return f"{self.dateStamp} ({self.count})"

class UserMinifigNotes:
    """
    This object is used to keep track of your notes for minifigs

    Attributes:
        minifigNumber : int 
            number of a minifigure
        notes : str 
            notes about particular minifigure
    """
    def __init__(self, minifigNumber:int, notes:str):
        """
        Initialization of userMinifigNotes class

        Args:
            minifigNumber : number of minifigure
            notes : notes about minifigure
        """
        self.minifigNumber = minifigNumber
        self.notes = notes
    def __str__(self):
        """
        String interpretation of userMinifigNotes class

        Returns:
            str : notes about minifigure  
        """
        return self.notes

class UserNotes:
    """
    Object to keep user's notes

    Attributes:
        setID : int
            ID of set, that notes are about
        notes : str
            Notes about particular set
    """
    def __init__(self, setID:int, notes:str):
        """
        Initialization of userNotes class

        Args:
            setID : ID of set, that notes are about
            notes : Notes about particular set
        """
        self.setID = setID
        self.notes = notes
    def __str__(self):
        """
        String interpretation of userMinifigNotes class

        Returns:
            str : notes about particular set  
        """
        return self.notes

class Instructions:
    """
    Class to keep track of instructions for sets

    Attributes:
        URL : str
            URL address of instruction for the set
        description : str
            Description of the set
    """
    def __init__(self, URL:str, description: str):
        """
        Initialization of instructions class

        Args:
            URL : URL address of instruction for the set
            description : Description of the set
        """
        self.URL = URL
        self.description = description
    def getInstructionsURL(self):
        """
        Get instruction's URL

        Returns:
            str : URL to instruction for set
        """
        return self.URL
    def downloadInstruction(self, location:str):
        """
        Downloads instruction for user
        
        Args: 
            location : specifies download location

        Returns:
            str: operation status
        """
        return 0
    def __str__(self):
        """
        String interpretation of instructions class

        Returns:
            str : description of the set
        """
        return self.description

class Years:
    """
    An object that tracks the total number of sets in year, theme

    Attributes:
        theme : str
            Theme of Lego
        year : int
            Year of Lego
        setCount : int
            Number of sets in specified year and theme
    """
    def __init__(self, theme:str, year:str, setCount:int):
        """
        Initialization of instructions class

        Args:
            URL : URL address of instruction for the set
            description : Description of the set
        """
        self.theme = theme
        self.year = year
        self.setCount = setCount
    def __str__(self):
        """
        String interpretation of instructions class

        Returns:
            str : the theme and year of specified class

        """
        return f"Set of {self.theme} from {self.year}"

class Subthemes:
    """
    A class to track subthemes of the theme

    Attributes:
        theme : str
            name of theme where subtheme is located
        subtheme : str
            name of subtheme
        setCount : int
            number of sets in subtheme
        yearFrom : int
            year from which subtheme was produced
        yearTo : int
            year to which subtheme was produced
     """
    def __init__(self, theme:str, subtheme:str, setCount:int, yearFrom:int, yearTo:int):
        """
        Initialization of subthemes class

        Args:
            theme : name of theme where subtheme is located
            subtheme : name of subtheme
            setCount : number of sets in subtheme
            yearFrom : year from which subtheme was produced
            yearTo : year till which subtheme was produced
        """
        self.theme = theme
        self.subtheme = subtheme
        self.setCount = setCount
        self.yearFrom = yearFrom
        self.yearTo = yearTo
    def __str__(self):
        """
        String interpretation of subthemes class

        Returns:
            str : name of subtheme and years of production
        """
        return f"{self.subtheme} produced in {self.yearFrom}-{self.yearTo}"

class Themes:
    """
    A class describing theme of Lego

    Attributes:
        theme : str
            name of Lego theme
        setCount : int
            number of sets in theme
        subthemeCount : int
            number of sets in subtheme
        yearFrom : int
            year from which theme was produced
        yearTo : int
            year till which theme was produced
    """
    def __init__(self, theme:str, setCount:int, subthemeCount:int, yearFrom:int, yearTo:int):
        """
        Initialization of theme class

        Attributes:
            theme : name of Lego theme
            setCount : number of sets in theme
            subthemeCount : number of sets in subtheme
            yearFrom : year from which theme was produced
            yearTo : year till which theme was produced
        """
        self.theme = theme
        self.setCount = setCount
        self.subthemeCount = subthemeCount
        self.yearFrom = yearFrom
        self.yearTo = yearTo
    def __str__(self):
        """
        String interpretation of themes class

        Returns:
            str : name of theme and years of its production
        """
        return f"{self.theme} produced in {self.yearFrom}-{self.yearTo}"

class MinifigCollection:
    """
    Data about minifigure collections
    
    Attributes:
        minifigNumber : str
            number of minifig
        name : str
            name of minifigure collection
        category : str
            name of the category
        ownedInSets : int
            number of minifigures owned from Lego sets
        ownedLoose : int
            number if minifigures owned outside of sets
        ownedTotal : int
            number of all minifigures
        wanted : bool
            tick if collection is wanted

    """
    def __init__(self, minifigNumber:str, name:str, category:str, ownedInSets:int, ownedLoose:int, ownedTotal:int, wanted:bool):
        """
            Initialization of minifigCollection class

            Args:
                minifigNumber : number of minifig
                name : name of minifigure collection
                category : name of the category
                ownedInSets : number of minifigures owned from Lego sets
                ownedLoose : number if minifigures owned outside of sets
                ownedTotal : number of all minifigures
                wanted : tick if collection is wanted
        """
        self.minifigNumber = minifigNumber
        self.name = name
        self.category = category
        self.ownedInSets = ownedInSets
        self.ownedLoose = ownedLoose
        self.ownedTotal = ownedTotal
        self.wanted = wanted
    def __str__(self):
        """
        String interpretation of minifigCollection class

        Returns:
            str : number of owned minifigure in collection
        """
        return f"{self.ownedTotal} in {self.name} collection"

class Rating:
    """
    Data about set

    Attributes:
        overall : int
            overall rating of set
        parts : int
            number of parts in set
        buildingExperience : int
            measurment stating how buildable set is
        playability : int
            measurment of how playable set is
        valueForMoney : int
            how valuable the set is for its price
    """
    def __init__(self, overall:int, parts:int, buildingExperience:int, playability:int, valueForMoney:int):
        """
        Initialization of rating class

        Args:
            overall : overall rating of set
            parts : number of parts in set
            buildingExperience : measurment stating how buildable set is
            playability : measurment of how playable set is
            valueForMoney : how valuable the set is for its price
        """
        self.overall = overall
        self.parts = parts
        self.buildingExperience = buildingExperience
        self.playability = playability
        self.valueForMoney = valueForMoney
    def __str__(self):
        """
        String interpretation of rating class

        Returns:
            str : the overall rating of set
        """
        return f"{self.overall}"

class Reviews:
    """
    Class that describes the reviews left about Lego sets
    
    Attributes:
        author : str
            the author of the review
        datePosted : date
            the date review was posted on
        rating : rating
            rating of the review
        title : str
            title of the review
        HTML : bool
            Checks if the review is HTML compatible
    """
    def __init__(self, author:str, datePosted:date, rating: Rating, title:str, review:str,HTML:bool):
        """
        Initialization of reviews class

        Args:
            author : the author of the review
            datePosted : the date review was posted on
            rating : rating of the review
            title : title of the review
            HTML : Checks if the review is HTML compatible
        """
        self.author = author
        self.datePosted = datePosted
        self.rating = rating
        self.title = title
        self.review = review
        self.HTML = HTML
    def __str__(self):
        """
        String interpretation of reviews class

        Returns:
            str : the review with title
        """
        return f"{self.title}: {self.review}"

class Image:
    """
    Image class containing thumbnail and image

    Attributes:
        thumbnailURL : str
            small picture URL
        imageURL : str
            URL of an image
    """
    def __init__(self, thumbnailURL:str, imageURL:str):
        """
        Initialization of image Class

        Args:
            thumbnailURL : small picture URL
            imageURL : URL of an image
        """
        self.thumbnailURL = thumbnailURL
        self.imageURL = imageURL
    def __str__(self):
        """
        String interpretation of image class

        Returns:
            str : returns imageURL
        """
        return self.imageURL

class AgeRange:
    """
    Age range for Lego sets

    Attributes:
        min_s : int ?
            minimal age requirement for Lego set
        max_s : int ?
            maximum age requirement for Lego set
    """
    def __init__(self,min_s:int|None, max_s:int|None):
        """
        Initialization of ageRange class

        Attributes:
            min_s : minimal age requirement for Lego set - may be -1 - means None
            max_s : maximum age requirement for Lego set - may be -1 - means None
        """
        if min_s is not None:
            self.min_s = min_s
        if max_s is not None:
            self.max_s = max_s
    def __str__(self):
        """
        String interpretation of ageRange class

        Returns:
            str : age requirements for set 
        """
        if self.min_s is not None:
            return f"{self.min_s}"
        if self.max_s is not None:
            return f"{self.max_s}"
        if (self.min_s is not None) and (self.max_s is not None):
            return f"{self.min_s} - {self.max_s}"
        return "No age requirement"

class Barcodes:
    """
    Class for keeping barcodes

    Attributes:
        EAN : str
            EAN type barcode
        UPC : str
            UPC type barcode
    """
    def __init__(self, EAN:str, UPC:str):
        """
        Initialization of barcodes class

        Args:
            EAN : EAN type barcode
            UPC : UPC type barcode
        """
        self.EAN = EAN
        self.UPC = UPC
    def __str__(self):
        """
        String interpretation of barcodes class

        Returns:
            str : EAN and UPC barcodes separated by whitespace
        """
        return f"EAN:{self.EAN} UPC:{self.UPC}"

class Collections:
    """
    Statistic data about Lego collections

    Attributes:
        ownedBy : int ?
            number of sets owned by user
        wantedBy : int ?
            number of sets wanted by user
    """
    def __init__(self, ownedBy:int|None, wantedBy:int|None):
        """
        Initialization of collections class

        Args:
            ownedBy : number of sets owned by user
            wantedBy : number of sets wanted by user

        """
        if ownedBy is not None:
            self.ownedBy = ownedBy
        if wantedBy is not None:
            self.wantedBy = wantedBy
    def __str__(self):
        """
        String interpretation of collections class

        Returns:
            str : number of owned and wanted sets by user
        """
        if (self.ownedBy is not None) and (self.wantedBy is not None):
            return f"Owned: {self.ownedBy}\nWanted: {self.wantedBy}"
        if self.ownedBy is not None:
            return f"Owned: {self.ownedBy}"
        if self.wantedBy is not None:
            return f"wanted {self.wantedBy}"
        return "No sets owned or wanted by user"

class Collection:
    """
    Class describes collection of Lego based on user

    Attributes:
        owned : bool ?
            check if user already owns the collection
        wanted : bool ?
            check if collection is wanted
        qtyOwned : int ?
            number of owned sets in the collection
        rating : int ?
            rating of the collection
        notes : str
            notes about the collection
    """
    def __init__(self, owned:bool|None, wanted:bool|None, qtyOwned:int|None, rating:int|None, notes:str):
        """
        Initialization of collection class

        Args:
            owned : check if user already owns the collection
            wanted : check if collection is wanted
            qtyOwned : number of owned sets in the collection
            rating : rating of the collection
            notes : notes about the collection
        """
        self.owned = owned
        self.wanted = wanted
        self.qtyOwned = qtyOwned
        self.rating = rating
        self.notes = notes
    def __str__(self):
        """
        String interpretation of collection class

        Returns: 
            str : notes for collection
        """
        return self.notes

class ExtendedData:
    """
    Some more data

    Attributes:
        notes : str
            notes from extendedData
        tags : list[str]
            tags list
        description : str
            short description
    """
    def __init__(self, notes:str, tags:list[str], description:str):
        """
        Initialization of extendedData class

        Args:
            notes : notes from extendedData
            tags : tags list
            description : short description
        """
        self.notes = notes
        self.tags = tags
        self.description = description
    def __str__(self):
        """
        String interpretation of extendedData class
        
        Returns:
            str : description from extendedData
        """
        return self.description

class Dimensions:
    """
    Size of the Lego set 

    Attributes:
        height : int ?
            height of the set
        width : int ?
            width of the set
        depth : int ?
            depth of the set
        weight : int ?
            weight of the set
    """
    def __init__(self, height:int|None, width:int|None, depth:int|None, weight:int|None):
        """
        Initialization of dimensions class
        
        Args:
            height : height of the set
            width : width of the set
            depth : depth of the set
            weight : weight of the set
        """
        self.height = height
        self.width = width
        self.depth = depth
        self.weight = weight
    def __str__(self):
        """
        String interpretation of dimensions class

        Returns:
            str : dimensions of the set XxYxZ  and weight or just XYZ or just weight 
        """
        if (self.height is not None) and (self.width is not None) and (self.depth is not None) and (self.weight is not None):
            return f"{self.height}x{self.width}x{self.depth} and weights {self.weight}"
        if (self.height is not None) and (self.width is not None) and (self.depth is not None):
            return f"{self.height}x{self.width}x{self.depth}"
        if self.weight is not None:
            return f"Weights {self.weight}"
        return ""

class LEGOComDetails:
    """
    Details about set from Lego.com

    Attributes:
        retailPrice : int ?
            price of the set in the shop
        dateFirstAvailable : date ?
            first time the set was available
        dateLastAvailable : date ?
            last time the set was available
    """
    def __init__(self, retailPrice:int|None, dateFirstAvailable:date|None, dateLastAvailable:date|None):
        """
        Initialization of LEGOComDetails class

        Args:
            retailPrice : price of the set in the shop
            dateFirstAvailable : first time the set was available
            dateLastAvailable : last time the set was available
        """
        self.retailPrice = retailPrice
        self.dateFirstAvailable = dateFirstAvailable
        self.dateLastAvailable = dateLastAvailable
    def __str__(self):
        if (self.retailPrice is not None) and (self.dateFirstAvailable is not None) and (self.dateLastAvailable is not None):
            return f"Was available from {self.dateFirstAvailable} to {self.dateLastAvailable} and cost {self.retailPrice}"
        if self.retailPrice is not None:
            return f"Costs {self.retailPrice}"
        return "No info available from LEGO.com"

class LEGOCom:
    """
    Collection of Lego.com data for different countries

    Attributes:
        US : LEGOComDetails
            data for United States
        UK : LEGOComDetails
            data for united Kingdom
        CA : LEGOComDetails
            data for Canada
        DE : LEGOComDetails
            data for Germany
    """
    def __init__(self, US:LEGOComDetails, UK:LEGOComDetails,CA:LEGOComDetails,DE:LEGOComDetails):
        """
        Initialization of LEGOCom class

        Args:
            US : data for United States
            UK : data for united Kingdom
            CA : data for Canada
            DE : data for Germany
        """
        self.US = US
        self.UK = UK
        self.CA = CA
        self.DE = DE
    def __str__(self):
        """
        String interpretation of LEGOCom class

        Returns:
            str : all providers
        """
        return f"US: {self.US}\nUK: {self.UK}\nCA: {self.CA}\nDE: {self.DE}"

class Sets:
    """
    Set description - the main class

    Attributes:
        setID : int
            ID of Lego set
        number : string
            number of Lego set
        numberVariant : int
            number number
        name : str
            name of Lego set
        year : int
            year of creation lego set
        theme : str
            theme name of Lego set
        themeGroup : str
            name of theme group of Lego set
        subtheme : str
            name of the subtheme of Lego set
        category : str
            name of the category of Lego set
        released : bool
            check if Lego set already exists
        pieces : int ?
            number of pieces in Lego set
        minifigs : int ?
            number of minifigs in Lego set
        image : Image
            image of Lego set
        bricksetURL : str
            URL to the Lego set on the brickset website
        collection : Collection
            collection of the Lego set
        collections : Collections
            collections of the Lego set
        legoCom : LEGOCom
            data from Lego.com website
        rating : int
            rating of Lego set
        reviewCount : int
            number of reviews
        packagingType : str
            chooses how the set is packaged
        availability : str
            check the availability of Lego set
        instructionsCount : int
            number of instructions in the Lego set
        additionalImageCount : int
            number of additional images for the Lego set
        ageRange : AgeRange
            range when Lego set was sold
        dimensions : Dimensions
            size and weight of Lego set
        barcode : Barcodes
            barcode of Lego set
        extendedData : ExtendedData
            some more data about Lego set
        lastUpdated : date
            last time Lego set data was updated
    """
    def __init__(self, setID:int, number:int, numberVariant:int, name:str, year:int, theme:str, themeGroup:str, subtheme:str, category:str, released:bool, pieces:int|None, minifigs:int|None, image:Image, bricksetURL:str, collection:Collection, collections:Collections, legoCom:LEGOCom, rating:int, reviewCount:int, packagingType:str, availability:str, instructionsCount:int, additionalImageCount:int, ageRange:AgeRange, dimensions:Dimensions, barcode:Barcodes, extendedData:ExtendedData, lastUpdated:date):
        """
        Initialization of set class

        Attributes:
        setID : ID of Lego set
        number : number of Lego set
        numberVariant : number number
        name : name of Lego set
        year : year of creation lego set
        theme : theme name of Lego set
        themeGroup : name of theme group of Lego set
        subtheme : name of the subtheme of Lego set
        category : name of the category of Lego set
        released : check if Lego set already exists
        pieces : number of pieces in Lego set
        minifigs : number of minifigs in Lego set
        image : image of Lego set
        bricksetURL : URL to the Lego set on the brickset website
        collection : collection of the Lego set
        collections : collections of the Lego set
        legoCom : data from Lego.com website
        rating : rating of Lego set
        reviewCount : number of reviews
        packagingType : chooses how the set is packaged
        availability : check the availability of Lego set
        instructionsCount : number of instructions in the Lego set
        additionalImageCount : number of additional images for the Lego set
        ageRange : range when Lego set was sold
        dimensions : size and weight of Lego set
        barcode : barcode of Lego set
        extendedData : some more data about Lego set
        lastUpdated : last time Lego set data was updated
        """
        self.setID =setID
        self.number = number
        self.numberVariant = numberVariant
        self.name = name
        self.year = year
        self.theme = theme
        self.themeGroup = themeGroup
        self.subtheme = subtheme
        self.category = category
        self.released = released
        self.pieces = pieces
        self.minifigs = minifigs
        self.image = image
        self.bricksetURL = bricksetURL
        self.collection = collection
        self.collections = collections
        self.legoCom = legoCom
        self.rating = rating
        self.reviewCount = reviewCount
        self.packagingType = packagingType
        self.availability = availability
        self.instructionsCount = instructionsCount
        self.additionalImageCount = additionalImageCount
        self.ageRange = ageRange
        self.dimensions = dimensions
        self.barcode = barcode
        self.extendedData = extendedData
        self.lastUpdated = lastUpdated
    def __str__(self):
        """
        String interpretation of Sets class

        Returns:
            str : set name
        """
        return self.name
