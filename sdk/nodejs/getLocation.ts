// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Use this data source to access information about a [Location](https://docs.controlplane.com/reference/location) within Control Plane.
 *
 * ## Required
 *
 * - **name** (String) Name of the location (i.e. `aws-us-west-2`).
 *
 * ## Outputs
 *
 * The following attributes are exported:
 *
 * - **cpln_id** (String) The ID, in GUID format, of the location.
 * - **name** (String) Name of the location.
 * - **description** (String) Description of the location.
 * - **tags** (Map of String) Key-value map of resource tags.
 * - **cloud_provider** (String) Cloud Provider of the location.
 * - **region** (String) Region of the location.
 * - **enabled** (Boolean) Indication if location is enabled.
 * - **geo** (Block List, Max: 1) (see below)
 * - **ip_ranges** (List of String) A list of IP ranges of the location.
 * - **self_link** (String) Full link to this resource. Can be referenced by other resources.
 *
 * <a id="nestedblock--geo"></a>
 *
 * ### `geo`
 *
 * Location geographical details
 *
 * - **lat** (Number) Latitude.
 * - **lon** (Number) Longitude.
 * - **country** (String) Country.
 * - **state** (String) State.
 * - **city** (String) City.
 * - **continent** (String) Continent.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as cpln from "@pulumi/cpln";
 *
 * const locationLocation = cpln.getLocation({
 *     name: "aws-us-west-2",
 * });
 * export const location = locationLocation;
 * export const locationEnabled = locationLocation.then(locationLocation => locationLocation.enabled);
 * ```
 */
export function getLocation(args: GetLocationArgs, opts?: pulumi.InvokeOptions): Promise<GetLocationResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("cpln:index/getLocation:getLocation", {
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getLocation.
 */
export interface GetLocationArgs {
    name: string;
}

/**
 * A collection of values returned by getLocation.
 */
export interface GetLocationResult {
    readonly cloudProvider: string;
    readonly cplnId: string;
    readonly description: string;
    readonly enabled: boolean;
    readonly geos: outputs.GetLocationGeo[];
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly ipRanges: string[];
    readonly name: string;
    readonly region: string;
    readonly selfLink: string;
    readonly tags: {[key: string]: string};
}
/**
 * Use this data source to access information about a [Location](https://docs.controlplane.com/reference/location) within Control Plane.
 *
 * ## Required
 *
 * - **name** (String) Name of the location (i.e. `aws-us-west-2`).
 *
 * ## Outputs
 *
 * The following attributes are exported:
 *
 * - **cpln_id** (String) The ID, in GUID format, of the location.
 * - **name** (String) Name of the location.
 * - **description** (String) Description of the location.
 * - **tags** (Map of String) Key-value map of resource tags.
 * - **cloud_provider** (String) Cloud Provider of the location.
 * - **region** (String) Region of the location.
 * - **enabled** (Boolean) Indication if location is enabled.
 * - **geo** (Block List, Max: 1) (see below)
 * - **ip_ranges** (List of String) A list of IP ranges of the location.
 * - **self_link** (String) Full link to this resource. Can be referenced by other resources.
 *
 * <a id="nestedblock--geo"></a>
 *
 * ### `geo`
 *
 * Location geographical details
 *
 * - **lat** (Number) Latitude.
 * - **lon** (Number) Longitude.
 * - **country** (String) Country.
 * - **state** (String) State.
 * - **city** (String) City.
 * - **continent** (String) Continent.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as cpln from "@pulumi/cpln";
 *
 * const locationLocation = cpln.getLocation({
 *     name: "aws-us-west-2",
 * });
 * export const location = locationLocation;
 * export const locationEnabled = locationLocation.then(locationLocation => locationLocation.enabled);
 * ```
 */
export function getLocationOutput(args: GetLocationOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetLocationResult> {
    return pulumi.output(args).apply((a: any) => getLocation(a, opts))
}

/**
 * A collection of arguments for invoking getLocation.
 */
export interface GetLocationOutputArgs {
    name: pulumi.Input<string>;
}