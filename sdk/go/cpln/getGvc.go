// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cpln

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
	"github.com/pulumiverse/pulumi-cpln/sdk/go/cpln/internal"
)

// Use this data source to access information about an existing [Global Virtual Cloud (GVC)](https://docs.controlplane.com/reference/gvc) within Control Plane.
//
// ## Required
//
// - **name** (String) Name of the GVC.
//
// ## Outputs
//
// The following attributes are exported:
//
// - **cpln_id** (String) The ID, in GUID format, of the GVC.
// - **name** (String) Name of the GVC.
// - **locations** (List of String) A list of [locations](https://docs.controlplane.com/reference/location#current) making up the Global Virtual Cloud.
// - **description** (String) Description of the GVC.
// - **domain** (String) Custom domain name used by associated workloads.
// - **pull_secrets** (List of String) A list of [pull secret](https://docs.controlplane.com/reference/gvc#pull-secrets) names used to authenticate to any private image repository referenced by Workloads within the GVC.
// - **tags** (Map of String) Key-value map of resource tags.
// - **lightstep_tracing** (Block List, Max: 1) (see below).
// - **self_link** (String) Full link to this resource. Can be referenced by other resources.
//
// <a id="nestedblock--lightstep_tracing"></a>
// ### `lightstepTracing`
//
// - **sampling** (Int) Sampling percentage.
// - **endpoint** (String) Tracing Endpoint Workload. Either the canonical endpoint or the internal endpoint.
// - **credentials** (String) Full link to referenced Opaque Secret.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//	"github.com/pulumiverse/pulumi-cpln/sdk/go/cpln"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			gvc, err := cpln.LookupGvc(ctx, nil, nil)
//			if err != nil {
//				return err
//			}
//			ctx.Export("gvcId", gvc.Id)
//			ctx.Export("gvcLocations", gvc.Locations)
//			return nil
//		})
//	}
//
// ```
func LookupGvc(ctx *pulumi.Context, args *LookupGvcArgs, opts ...pulumi.InvokeOption) (*LookupGvcResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupGvcResult
	err := ctx.Invoke("cpln:index/getGvc:getGvc", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getGvc.
type LookupGvcArgs struct {
	ControlplaneTracing *GetGvcControlplaneTracing `pulumi:"controlplaneTracing"`
	Description         *string                    `pulumi:"description"`
	// Deprecated: Selecting a domain on a GVC will be deprecated in the future. Use the 'cpln_domain resource' instead.
	Domain           *string                 `pulumi:"domain"`
	Env              map[string]string       `pulumi:"env"`
	LightstepTracing *GetGvcLightstepTracing `pulumi:"lightstepTracing"`
	LoadBalancer     *GetGvcLoadBalancer     `pulumi:"loadBalancer"`
	Locations        []string                `pulumi:"locations"`
	Name             string                  `pulumi:"name"`
	OtelTracing      *GetGvcOtelTracing      `pulumi:"otelTracing"`
	PullSecrets      []string                `pulumi:"pullSecrets"`
	Sidecar          *GetGvcSidecar          `pulumi:"sidecar"`
	Tags             map[string]string       `pulumi:"tags"`
}

// A collection of values returned by getGvc.
type LookupGvcResult struct {
	Alias               string                     `pulumi:"alias"`
	ControlplaneTracing *GetGvcControlplaneTracing `pulumi:"controlplaneTracing"`
	CplnId              string                     `pulumi:"cplnId"`
	Description         *string                    `pulumi:"description"`
	// Deprecated: Selecting a domain on a GVC will be deprecated in the future. Use the 'cpln_domain resource' instead.
	Domain *string           `pulumi:"domain"`
	Env    map[string]string `pulumi:"env"`
	// The provider-assigned unique ID for this managed resource.
	Id               string                  `pulumi:"id"`
	LightstepTracing *GetGvcLightstepTracing `pulumi:"lightstepTracing"`
	LoadBalancer     *GetGvcLoadBalancer     `pulumi:"loadBalancer"`
	Locations        []string                `pulumi:"locations"`
	Name             string                  `pulumi:"name"`
	OtelTracing      *GetGvcOtelTracing      `pulumi:"otelTracing"`
	PullSecrets      []string                `pulumi:"pullSecrets"`
	SelfLink         string                  `pulumi:"selfLink"`
	Sidecar          *GetGvcSidecar          `pulumi:"sidecar"`
	Tags             map[string]string       `pulumi:"tags"`
}

func LookupGvcOutput(ctx *pulumi.Context, args LookupGvcOutputArgs, opts ...pulumi.InvokeOption) LookupGvcResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupGvcResult, error) {
			args := v.(LookupGvcArgs)
			r, err := LookupGvc(ctx, &args, opts...)
			var s LookupGvcResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupGvcResultOutput)
}

// A collection of arguments for invoking getGvc.
type LookupGvcOutputArgs struct {
	ControlplaneTracing GetGvcControlplaneTracingPtrInput `pulumi:"controlplaneTracing"`
	Description         pulumi.StringPtrInput             `pulumi:"description"`
	// Deprecated: Selecting a domain on a GVC will be deprecated in the future. Use the 'cpln_domain resource' instead.
	Domain           pulumi.StringPtrInput          `pulumi:"domain"`
	Env              pulumi.StringMapInput          `pulumi:"env"`
	LightstepTracing GetGvcLightstepTracingPtrInput `pulumi:"lightstepTracing"`
	LoadBalancer     GetGvcLoadBalancerPtrInput     `pulumi:"loadBalancer"`
	Locations        pulumi.StringArrayInput        `pulumi:"locations"`
	Name             pulumi.StringInput             `pulumi:"name"`
	OtelTracing      GetGvcOtelTracingPtrInput      `pulumi:"otelTracing"`
	PullSecrets      pulumi.StringArrayInput        `pulumi:"pullSecrets"`
	Sidecar          GetGvcSidecarPtrInput          `pulumi:"sidecar"`
	Tags             pulumi.StringMapInput          `pulumi:"tags"`
}

func (LookupGvcOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupGvcArgs)(nil)).Elem()
}

// A collection of values returned by getGvc.
type LookupGvcResultOutput struct{ *pulumi.OutputState }

func (LookupGvcResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupGvcResult)(nil)).Elem()
}

func (o LookupGvcResultOutput) ToLookupGvcResultOutput() LookupGvcResultOutput {
	return o
}

func (o LookupGvcResultOutput) ToLookupGvcResultOutputWithContext(ctx context.Context) LookupGvcResultOutput {
	return o
}

func (o LookupGvcResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupGvcResult] {
	return pulumix.Output[LookupGvcResult]{
		OutputState: o.OutputState,
	}
}

func (o LookupGvcResultOutput) Alias() pulumi.StringOutput {
	return o.ApplyT(func(v LookupGvcResult) string { return v.Alias }).(pulumi.StringOutput)
}

func (o LookupGvcResultOutput) ControlplaneTracing() GetGvcControlplaneTracingPtrOutput {
	return o.ApplyT(func(v LookupGvcResult) *GetGvcControlplaneTracing { return v.ControlplaneTracing }).(GetGvcControlplaneTracingPtrOutput)
}

func (o LookupGvcResultOutput) CplnId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupGvcResult) string { return v.CplnId }).(pulumi.StringOutput)
}

func (o LookupGvcResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupGvcResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

// Deprecated: Selecting a domain on a GVC will be deprecated in the future. Use the 'cpln_domain resource' instead.
func (o LookupGvcResultOutput) Domain() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupGvcResult) *string { return v.Domain }).(pulumi.StringPtrOutput)
}

func (o LookupGvcResultOutput) Env() pulumi.StringMapOutput {
	return o.ApplyT(func(v LookupGvcResult) map[string]string { return v.Env }).(pulumi.StringMapOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o LookupGvcResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupGvcResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o LookupGvcResultOutput) LightstepTracing() GetGvcLightstepTracingPtrOutput {
	return o.ApplyT(func(v LookupGvcResult) *GetGvcLightstepTracing { return v.LightstepTracing }).(GetGvcLightstepTracingPtrOutput)
}

func (o LookupGvcResultOutput) LoadBalancer() GetGvcLoadBalancerPtrOutput {
	return o.ApplyT(func(v LookupGvcResult) *GetGvcLoadBalancer { return v.LoadBalancer }).(GetGvcLoadBalancerPtrOutput)
}

func (o LookupGvcResultOutput) Locations() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupGvcResult) []string { return v.Locations }).(pulumi.StringArrayOutput)
}

func (o LookupGvcResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupGvcResult) string { return v.Name }).(pulumi.StringOutput)
}

func (o LookupGvcResultOutput) OtelTracing() GetGvcOtelTracingPtrOutput {
	return o.ApplyT(func(v LookupGvcResult) *GetGvcOtelTracing { return v.OtelTracing }).(GetGvcOtelTracingPtrOutput)
}

func (o LookupGvcResultOutput) PullSecrets() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupGvcResult) []string { return v.PullSecrets }).(pulumi.StringArrayOutput)
}

func (o LookupGvcResultOutput) SelfLink() pulumi.StringOutput {
	return o.ApplyT(func(v LookupGvcResult) string { return v.SelfLink }).(pulumi.StringOutput)
}

func (o LookupGvcResultOutput) Sidecar() GetGvcSidecarPtrOutput {
	return o.ApplyT(func(v LookupGvcResult) *GetGvcSidecar { return v.Sidecar }).(GetGvcSidecarPtrOutput)
}

func (o LookupGvcResultOutput) Tags() pulumi.StringMapOutput {
	return o.ApplyT(func(v LookupGvcResult) map[string]string { return v.Tags }).(pulumi.StringMapOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupGvcResultOutput{})
}