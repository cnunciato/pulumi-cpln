// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Cpln
{
    public static class GetLocations
    {
        /// <summary>
        /// Use this data source to access information about all [Locations](https://docs.controlplane.com/reference/location) within Control Plane.
        /// 
        /// ## Outputs
        /// 
        /// The following attributes are exported:
        /// 
        /// - **locations** (Block List, Max: 1) (see below).
        /// 
        /// &lt;a id="nestedblock--locations"&gt;&lt;/a&gt;
        /// 
        /// ### `locations`
        /// 
        /// - **cpln_id** (String) The ID, in GUID format, of the location.
        /// - **name** (String) Name of the location.
        /// - **description** (String) Description of the location.
        /// - **tags** (Map of String) Key-value map of resource tags.
        /// - **cloud_provider** (String) Cloud Provider of the location.
        /// - **region** (String) Region of the location.
        /// - **enabled** (Boolean) Indication if location is enabled.
        /// - **geo** (Block List, Max: 1) (see below)
        /// - **ip_ranges** (List of String) A list of IP ranges of the location.
        /// - **self_link** (String) Full link to this resource. Can be referenced by other resources.
        /// 
        /// &lt;a id="nestedblock--geo"&gt;&lt;/a&gt;
        /// 
        /// ### `geo`
        /// 
        /// Location geographical details
        /// 
        /// - **lat** (Number) Latitude.
        /// - **lon** (Number) Longitude.
        /// - **country** (String) Country.
        /// - **state** (String) State.
        /// - **city** (String) City.
        /// - **continent** (String) Continent.
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Cpln = Pulumi.Cpln;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var locationsLocations = Cpln.GetLocations.Invoke();
        /// 
        ///     return new Dictionary&lt;string, object?&gt;
        ///     {
        ///         ["locations"] = locationsLocations.Apply(getLocationsResult =&gt; getLocationsResult.Locations),
        ///     };
        /// });
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetLocationsResult> InvokeAsync(InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetLocationsResult>("cpln:index/getLocations:getLocations", InvokeArgs.Empty, options.WithDefaults());

        /// <summary>
        /// Use this data source to access information about all [Locations](https://docs.controlplane.com/reference/location) within Control Plane.
        /// 
        /// ## Outputs
        /// 
        /// The following attributes are exported:
        /// 
        /// - **locations** (Block List, Max: 1) (see below).
        /// 
        /// &lt;a id="nestedblock--locations"&gt;&lt;/a&gt;
        /// 
        /// ### `locations`
        /// 
        /// - **cpln_id** (String) The ID, in GUID format, of the location.
        /// - **name** (String) Name of the location.
        /// - **description** (String) Description of the location.
        /// - **tags** (Map of String) Key-value map of resource tags.
        /// - **cloud_provider** (String) Cloud Provider of the location.
        /// - **region** (String) Region of the location.
        /// - **enabled** (Boolean) Indication if location is enabled.
        /// - **geo** (Block List, Max: 1) (see below)
        /// - **ip_ranges** (List of String) A list of IP ranges of the location.
        /// - **self_link** (String) Full link to this resource. Can be referenced by other resources.
        /// 
        /// &lt;a id="nestedblock--geo"&gt;&lt;/a&gt;
        /// 
        /// ### `geo`
        /// 
        /// Location geographical details
        /// 
        /// - **lat** (Number) Latitude.
        /// - **lon** (Number) Longitude.
        /// - **country** (String) Country.
        /// - **state** (String) State.
        /// - **city** (String) City.
        /// - **continent** (String) Continent.
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Cpln = Pulumi.Cpln;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var locationsLocations = Cpln.GetLocations.Invoke();
        /// 
        ///     return new Dictionary&lt;string, object?&gt;
        ///     {
        ///         ["locations"] = locationsLocations.Apply(getLocationsResult =&gt; getLocationsResult.Locations),
        ///     };
        /// });
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetLocationsResult> Invoke(InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetLocationsResult>("cpln:index/getLocations:getLocations", InvokeArgs.Empty, options.WithDefaults());
    }


    [OutputType]
    public sealed class GetLocationsResult
    {
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly ImmutableArray<Outputs.GetLocationsLocationResult> Locations;

        [OutputConstructor]
        private GetLocationsResult(
            string id,

            ImmutableArray<Outputs.GetLocationsLocationResult> locations)
        {
            Id = id;
            Locations = locations;
        }
    }
}
